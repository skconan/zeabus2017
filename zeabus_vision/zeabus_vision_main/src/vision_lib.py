#!/usr/bin/env python
import cv2
import numpy as np
import math
import rospy
from sensor_msgs.msg import CompressedImage, Image
from cv_bridge import CvBridge, CvBridgeError
from matplotlib import pyplot as plt
import statistics
image = None


def range_str2list(str):
    str = str.split(',')
    return np.array([int(str[0]), int(str[1]), int(str[2])], np.uint8)


def delete_color(hsv, color, camera):
    lower, upper = getColor(color, camera)
    print lower
    print upper
    if not lower is None:
        res = cv2.inRange(hsv, lower, upper)
    else:
        h, s, v = cv2.split(hsv)
        ret, res = cv2.threshold(v, 127, 255, cv2.THRESH_BINARY)
    return res


def getColor(color, camera):
    # Navigate
    lower = None
    upper = None
    color_list_down = ['orange', 'white', 'yellow', 'red']
    color_list_top = ['orange', 'white', 'yellow', 'red']

    for c in color_list_down:
        if color == c:
            lower = rospy.get_param(
                '/color_range/color_' + camera + '/lower_' + c)
            upper = rospy.get_param(
                '/color_range/color_' + camera + '/upper_' + c)

    if not lower is None:
        lower = range_str2list(lower)
        upper = range_str2list(upper)
    return lower, upper


def find_shape(cnt, req):
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
    if len(approx) == 3 and req == 'tri':
        return True
    elif len(approx) == 4 and req == 'rect':
        return True
    elif len(approx) >= 10 and req == 'cir':
        return True
    elif len(approx) == req:
        return True
    return False


def cut_contours(M, w, h, range_w, range_h):
    cx = None
    cy = None
    try:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
    except:
        print 'err'
    if cx is None:
        return True
    if cx <= range_w or cy <= range_h or cx >= w - range_w or cy >= h - range_h:
        return True
    return False


def equalization_bgr(imgBGR):
    b, g, r = cv2.split(imgBGR)
    b = cv2.equalizeHist(b)
    g = cv2.equalizeHist(g)
    r = cv2.equalizeHist(r)
    equBGR = cv2.merge((b, g, r))
    return equBGR


def equalization_hsv(imgHSV):
    h, s, v = cv2.split(imgHSV)
    v = cv2.equalizeHist(v)
    equHSV = cv2.merge((h, s, v))
    return equHSV


def equalization_gray(imgGRAY):
    equGRAY = cv2.equalizeHist(imgGRAY)

    return equGRAY


def clahe(imgBGR):
    lab = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2Lab)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))
    l = clahe.apply(l)
    lab = cv2.merge((l, a, b))
    resBGR = cv2.cvtColor(lab, cv2.COLOR_Lab2BGR)
    return resBGR


def stretching_hsv(hsv):
    h, s, v = cv2.split(hsv)

    if s.min() > 0:
        s *= int(round(255.0 / (s.max() - s.min())))
    if v.min() > 0:
        v *= int(round(255.0 / (v.max() - v.min())))
    hsv = cv2.merge((h, s, v))
    return hsv


def stretching_bgr(bgr):
    b, g, r = cv2.split(bgr)
    # b -= b.min()
    # b *= int(round(255.0 / (b.max() - b.min())))
    g -= g.min()
    g *= int(round(255.0 / (g.max() - g.min())))
    r -= r.min()
    r *= int(round(255.0 / (r.max() - r.min())))

    img = cv2.merge((b, g, r))
    return img


def stretching(img):

    b, g, r = cv2.split(img)
    b -= b.min()
    b *= int(round(255.0 / (b.max() - b.min())))
    g -= g.min()
    g *= int(round(255.0 / (g.max() - g.min())))
    r -= r.min()
    r *= int(round(255.0 / (g.max() - g.min())))

    img = cv2.merge((b, g, r))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(img)

    s -= s.min()
    s *= int(round(255.0 / (s.max() - s.min())))

    v -= v.min()
    v *= int(round(255.0 / (v.max() - v.min())))

    img = cv2.merge((h, s, v))
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

    return img


def cut_frame_top(imgBinary):
    # cut 1/4 of top of frame
    rows, cols = imgBinary.shape
    maskTop = np.zeros((int(rows / 4), cols))
    maskBottom = np.ones((int(3 * rows / 4), cols))
    res = np.concatenate((maskTop, maskBottom), axis=0)
    res = cv2.bitwise_and(res, res, mask=imgBinary)
    return res


def cut_frame_bottom(imgBinary):
    # cut 1/4 of bottom of frame
    rows, cols = imgBinary.shape
    maskTop = np.ones((int(3 * rows / 4), cols))
    maskBottom = np.zeros((int(rows / 4), cols))
    res = np.concatenate((maskTop, maskBottom), axis=0)
    res = cv2.bitwise_and(res, res, mask=imgBinary)
    return res


def Oreintation(moment):
    tmp = pow((moment['mu20'] - moment['mu02']), 2)
    tmp = math.sqrt(tmp + (4 * pow(moment['mu11'], 2)))

    k = moment['mu02'] - moment['mu20']

    l = 2 * moment['mu11']

    rad_maj = math.atan2(k + tmp, l)
    rad_min = math.atan2(k - tmp, l)
    return rad_maj, rad_min


def nothing(variable):
    pass


def get_mode(v):
    v = v.ravel()
    try:
        MODE = statistics.mode(v)
    except ValueError:
        MODE = 127

    return MODE


def rebalance(image):
    h, w, ch = image.shape
    m = cv2.mean(image)
    img = np.zeros((h, w), dtype=np.float)
    img = image.copy()
    b, g, r = cv2.split(img)

    gg = m[0] * 1.0 / m[1] * 1.0
    rr = m[0] * 1.0 / m[2] * 1.0

    matrix_b = np.zeros((h, w), dtype=np.float32)
    matrix_g = np.zeros((h, w), dtype=np.float32)
    matrix_r = np.zeros((h, w), dtype=np.float32)
    matrix_b.fill(1.0)
    matrix_g.fill(gg)
    matrix_r.fill(rr)

    b = b * matrix_b
    g = g * matrix_g
    r = r * matrix_r

    result = cv2.merge((b, g, r))
    result_uint = result.astype(np.uint8)

    # ____________________________ #

    img = cv2.cvtColor(result_uint, cv2.COLOR_BGR2Lab)
    L, a, b = cv2.split(img)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    L = clahe.apply(L)

    result = cv2.merge((L, a, b))
    result_bgr = cv2.cvtColor(result, cv2.COLOR_Lab2BGR)
    result_hsv = cv2.cvtColor(result_bgr, cv2.COLOR_BGR2HSV)
    # h, s, v = cv2.split(result_hsv)
    # print h.max(),s.max(),v.max()
    return result_hsv


def process_img_down(imgBGR):
    # bgr = stretching(imgBGR.copy())
    hsv = clahe(imgBGR.copy())
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    median = cv2.medianBlur(bgr.copy(), 7)
    hsv = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)

    return hsv


def process_img_top(img):
    bgr = stretching(img.copy())
    # hsv = clahe(bgr.copy())
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    return hsv


def shrinking_hsv(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    hmin = h.min()
    hmax = h.max()
    hl = 180
    hs = ((h - hmin) / (hmax - hmin)) * (hl - 1)

    smin = s.min()
    smax = s.max()
    sl = 255
    ss = ((s - smin) / (smax - smin)) * (sl - 1)

    vmin = v.min()
    vmax = v.max()
    vl = 255
    vs = ((v - vmin) / (vmax - vmin)) * (vl - 1)

    result = cv2.merge((hs, ss, vs))
    return result


def publish_result(img, type, topicName):
    if img is None:
        img = np.zeros((200, 200))
        type = "gray"
    bridge = CvBridge()
    pub = rospy.Publisher(
        topicName, Image, queue_size=10)
    if type == 'gray':
        msg = bridge.cv2_to_imgmsg(img, "mono8")
    elif type == 'bgr':
        msg = bridge.cv2_to_imgmsg(img, "bgr8")
    pub.publish(msg)


def adjust_gamma(imgBGR=None, gamma=1):
    if imgBGR is None:
        print('given value to imgBGR argument\n' +
              'adjust_gamma_by_value(imgBGR, gamma)')

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) *
                      255 for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(imgBGR, table)


def adjust_gamma_by_v(imgBGR=None):
    if imgBGR is None:
        print('given value to imgBGR argument\n' +
              'adjust_gamma_by_value(imgBGR, gamma)')
        return
    hsv = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    vMean = cv2.mean(v)[0]

    gamma = vMean / 13

    # print vMean
    gamma = vMean / 155
    # print 'gamma : ' + str(gamma)

    if gamma == 0:
        g = 1.0
    else:
        g = gamma / 10.0
    invGamma = 1.0 / g
    # print 'g : ' + str(g)
    table = []
    for i in np.arange(0, 256):
        table.append(((i / 255.0) ** invGamma) * 255)
    table = np.array(table).astype('uint8')
    res = cv2.LUT(imgBGR, table)
    return res


def get_kernal(shape='rect', ksize=(5, 5)):
    if shape == 'rect':
        return cv2.getStructuringElement(cv2.MORPH_RECT, ksize)
    elif shape == 'ellipse':
        return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)
    elif shape == 'plus':
        return cv2.getStructuringElement(cv2.MORPH_CROSS, ksize)
    else:
        return None


def erode(imgBin, ker):
    return cv2.erode(imgBin, ker, iterations=1)


def dilate(imgBin, ker):
    return cv2.dilate(imgBin, ker, iterations=1)


def close(imgBin, ker):
    return cv2.morphologyEx(imgBin, cv2.MORPH_CLOSE, ker)


def callback_raw(ros_data):
    global image
    width = 640
    height = 512
    bridge = CvBridge()
    image = cv2.resize(bridge.imgmsg_to_cv2(ros_data, "bgr8"), (width, height))


def callback_compressed(ros_data):
    global image
    width = 640
    height = 512
    np_arr = np.fromstring(ros_data.data, np.uint8)
    image = cv2.resize(cv2.imdecode(
        np_arr, 1), (width, height))

if __name__ == '__main__':
    rospy.init_node('vision_lib', anonymous=True)
    # sub = rospy.Subscriber('/top/center/image_rect_color', Image,
    #                        callback, queue_size=10)
    # sub = rospy.Subscriber('/leftcam_bottom/image_raw/compressed', CompressedImage,
    #                        callback1, queue_size=10)
    # sub = rospy.Subscriber('/top/center/image_rect_color/compressed', CompressedImage,
    #                        callback1, queue_size=10)HSVHSV
    sub = rospy.Subscriber('/bottom/left/image_raw/compressed', CompressedImage,
                           callback_compressed, queue_size=10)
    plt.ion()
    while not rospy.is_shutdown():
        if image is None:
            continue

        claheimg = clahe(image)
        # equBGR = equalization_bgr(image)
        hsv = cv2.cvtColor(claheimg, cv2.COLOR_BGR2HSV)
        equHSV = equalization_hsv(hsv)
        bgr = cv2.cvtColor(equHSV, cv2.COLOR_HSV2BGR)

        cv2.imshow('image', bgr)
        # cv2.imshow('equBGR', equBGR)
        cv2.imshow('hsv', hsv)
        cv2.imshow('equHSV', equHSV)
        h, s, v = cv2.split(hsv)

        k = cv2.waitKey(1) & 0xff
        if k == ord('q'):
            break
        rospy.sleep(0.1)
    cv2.destroyAllWindows()

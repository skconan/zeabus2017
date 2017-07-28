#!/usr/bin/env python
import cv2
import numpy as np
import rospkg
import rospy
import math
import sys
sys.path.append ('/home/zeabus/catkin_ws/src/src_code/zeabus_vision/zeabus_vision_main/src/')
from vision_lib import *
from sensor_msgs.msg import CompressedImage
from zeabus_vision_srv_msg.msg import vision_msg_default
from zeabus_vision_srv_msg.srv import vision_srv_default

img = None
height = None
width = None

def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0/gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
    for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)

def canny(image, threshold1, threshold2):
    return cv2.Canny(image, threshold1, threshold2)

def find_bin(msg):
    global img, width, height
    req = msg.req.data
    print('req', req)
    lowerOrange, upperOrange = get_color('orange', 'bottom', 'bin')
    lowerWhite, upperWhite = get_color('white', 'bottom', 'bin')
    res = vision_msg_default()

    ratio = -999

    while not rospy.is_shutdown():
        while img is None:
            print('None')

        offsetW = width/2
        offsetH = height/2

        image = img.copy()
        
        blackThreshold = 200

        imageForDraw = img.copy()

        cla = clahe(image)
        blur = cv2.bilateralFilter(cla, 15, 75, 75)
        blurClaGray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        blurClaGray = equalization_gray(blurClaGray)

        # imgBgr = preprocess_bin
        eqOrange = preprocess_bin(image)

        gray = cv2.cvtColor(eqOrange, cv2.COLOR_BGR2GRAY)

        eqOrange = cv2.cvtColor(eqOrange, cv2.COLOR_BGR2HSV)
        eqOrange = cv2.inRange(eqOrange, lowerOrange, upperOrange)
        
        # ret, black = cv2.threshold(blurClaGray, blackThreshold, 255, cv2.THRESH_BINARY_INV)
        # ret, black = cv2.threshold(gray, blackThreshold, 255, cv2.THRESH_BINARY_INV)
        ret, black = cv2.threshold(gray, blackThreshold, 255, cv2.THRESH_BINARY)

        black = open_morph(black, get_kernel('cross', (17,17)))
        # black = dilate(black, get_kernel('cross', (5,5)))
        black = erode(black, get_kernel('cross', (9,9)))
        black = erode(black, get_kernel('rect', (1,3)))

        
        orangeImage = close(eqOrange, get_kernel('rect',(15,15)))

        black = cv2.subtract(black, eqOrange)

        _, orangeContours, _ = cv2.findContours(orangeImage.copy(), 
                                            cv2.RETR_EXTERNAL, 
                                            cv2.CHAIN_APPROX_SIMPLE)
        _, blackContours, hierarchy = cv2.findContours(black.copy(), 
                                            cv2.RETR_EXTERNAL, 
                                            cv2.CHAIN_APPROX_SIMPLE)
        xBinCover = -999
        xBinNonCover = -999
        
        yBinCover = -999
        yBinNonCover = -999
        
        boxNoCover = image.copy().fill(0)
        boxCover = image.copy().fill(0)
        
        maxNoCover = 0
        maxCover = 0
        
        range_w = 25
        range_h = 25
        
        binAppear = False
        noCoverAppear = False
        
        noCoverAngle = -999
        coverAngle = -999

        offsetShootX = 25
        offsetShootY = 25
        for c in orangeContours:
            M = cv2.moments(c)
            rect = (x,y),(ww,hh),_ =cv2.minAreaRect(c)
            area = ww*hh
            
            if not find_shape(c, 'rect'):
                continue
            # if area < 500:
            #     continue
            if maxCover < area:
                maxCover = area
                xBinCover = x
                yBinCover = y
                boxCover = cv2.boxPoints(rect)
                boxCover = np.int0(boxCover)
                coverAngle = 90-Oreintation(M)[0]*180/math.pi
        
        cv2.drawContours(imageForDraw,[boxCover], -1,(0,255,0),1)
        cv2.circle(imageForDraw ,(int(xBinCover), int(yBinCover)), 5, (0, 255, 255), -1)
        for c in blackContours:
            M = cv2.moments(c)
            rect = (x,y),(ww,hh),_ = cv2.minAreaRect(c)
            area = ww*hh
            
            diffX = abs(xBinCover-x)
            diffY = abs(yBinCover-y)

            if diffX < 20 and diffY < 20:
                continue

            realArea = cv2.contourArea(c)
            

            if not find_shape(c, 'rect'):
                continue

            print('realArea',maxNoCover)

            if area < 2000:
                continue

            if ww > hh:
                temp = ww
                ww = hh
                hh = temp

            ratio = float(ww/hh)
            # if ratio > 0.7:
            #     continue

            if maxNoCover < realArea:
                maxNoCover = realArea
                boxNoCover = cv2.boxPoints(rect)
                boxNoCover = np.int0(boxNoCover)
                xBinNonCover = x
                yBinNonCover = y
                noCoverAngle = 90-Oreintation(M)[0]*180/math.pi
        # print('----------------------')

        # print(maxNoCover)

        print('=========================')

        cv2.drawContours(imageForDraw, [boxNoCover], -1, (255,255,255), 2)


        if maxCover > 0:
            binAppear = True
        if maxNoCover > 0:
            noCoverAppear = True

        # print('angle', noCoverAngle)

        # xBinNonCover -= offsetShootX

        if req == 'nocover': # **Note** swap x and y for AI 
            cv2.circle(imageForDraw ,(int(xBinNonCover), int(yBinNonCover)), 5, (0, 255, 255), -1)
            res.y = -(xBinNonCover-offsetW)/offsetW
            res.x = (offsetH-yBinNonCover)/offsetH
            res.angle = noCoverAngle
            res.appear = noCoverAppear
        elif req == 'bin':
            cv2.circle(imageForDraw ,(int(xBinCover), int(yBinCover)), 5, (0, 255, 255), -1)
            res.y = -(xBinCover-offsetW)/offsetW
            res.x = (offsetH-yBinCover)/offsetH
            res.angle = coverAngle
            res.appear = binAppear
        else:
            print('error no req')
        publish_result(imageForDraw, 'bgr', 'debug')
        # publish_result(blurClaGray, 'gray', 'blurClaGray')
        publish_result(blur, 'bgr', 'blur')
        publish_result(black, 'gray', 'black')
        publish_result(gray, 'gray', 'gray')

        print('ratio', ratio)

        if ratio > 0.8:
            res.appear = False
            print("not found")
        else:
            res.appear = True
            print("found")

        return res

def mission_callback(msg):
    print(msg.req.data)
    return find_bin(msg)

def img_callback(msg):
    global img, width, height
    arr = np.fromstring(msg.data, np.uint8)
    img = cv2.resize(cv2.imdecode(arr, 1), (640/2, 384/2))

    height, width, _ = img.shape
    

if __name__ == '__main__':
    rospy.init_node('isBin')
    bag = '/leftcam_bottom/image_raw/compressed'
    topic = '/bottom/left/image_raw/compressed'
    bot = '/bottom/left/image_raw/compressed'
    rospy.Subscriber(bot, CompressedImage, img_callback)
    # rospy.Subscriber(bag, CompressedImage, img_callback)
    # find_bin()
    rospy.Service('vision_where', vision_srv_default(), mission_callback)
    rospy.spin()
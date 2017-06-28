#!/usr/bin/env python
import cv2
import numpy as np
import rospkg
import rospy
import math
import sys
sys.path.append ('/home/zeabus/catkin_ws/src/src_code/zeabus_vision/main/src/')
from vision_lib import *
from sensor_msgs.msg import CompressedImage
from zeabus_vision_srv_msg.msg import vision_msg_navigate
from zeabus_vision_srv_msg.srv import vision_srv_navigate

img = None
width = None
height = None

img_bot = None
height_bot = None
width_bot = None


def rect_ker(x,y):
    return cv2.getStructuringElement(cv2.MORPH_RECT,(x,y))

def ellipse_ker(x,y):
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(x,y))

def cross_ker(x,y):
    return cv2.getStructuringElement(cv2.MORPH_CROSS,(x,y))

def erode(imgBin, ker):
    return cv2.erode(imgBin, ker, iterations = 1)

def dilate(imgBin, ker):
    return cv2.dilate(imgBin, ker, iterations =  1)

def close(imgBin, ker):
    return cv2.morphologyEx(imgBin, cv2.MORPH_CLOSE, ker)

def tophat(imgBin, ker):
    return cv2.morphologyEx(imgBin, cv2.MORPH_TOPHAT, ker)

def isVertical(x):
    global width
    temp = 40
    return (x<temp) or (x>width-temp)

def isHorizon(y):
    global height
    temp = 50
    return (y<temp) or (y>height-temp)

def not_center_bot(x):
    global width
    temp = 100
    return (x<temp) or (x>width-temp)

def navigate_top():
    global img, width, height
    im = None
    res = vision_msg_navigate()
    lower_yellow, upper_yellow = getColor('yellow', 'top') 
    while not rospy.is_shutdown():
        while img is None:
            print("img : None")
        height, width,_ = img.shape
        im_size = height*width
        offsetW = width/2
        offsetH = height/2
        im = img.copy()
        im_draw = img.copy()
        hsv = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2HSV)
        print('lower_yellow', lower_yellow)
        print('upper_yellow', upper_yellow)
        im_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
        
        im_delnoise = erode(im_yellow, cross_ker(3,3))
        im_delnoise = dilate(im_delnoise, cross_ker(3,3))
        im_delnoise2 = erode(im_yellow, cross_ker(5,1))
        im_lr = dilate(im_delnoise, rect_ker(15,1))
        im_lr = close(im_lr, rect_ker(11,11))
        im_lr = erode(im_lr, rect_ker(1,55))
        im_bot = dilate(im_delnoise2, rect_ker(1,23))
        im_bot = erode(im_bot, rect_ker(35, 1))
        
        plate = im_lr+im_bot
        _, contours_lr, hierarchy = cv2.findContours(im_lr.copy(), 
                                            cv2.RETR_TREE, 
                                            cv2.CHAIN_APPROX_SIMPLE)

        _, contours_bot, _ = cv2.findContours(im_bot.copy(), 
                                            cv2.RETR_TREE, 
                                            cv2.CHAIN_APPROX_SIMPLE)

        max = 0
        count_h = 0
        cx = 0
        cy = 0
        lr_x = -999
        area_h = 0
        area_w = 0
        area = -999
        direction = -999
        ratio_area = -999
        x_lr = -999
        x_bot = -999
        left = 0
        right = 0
        for c in contours_lr:
            M = cv2.moments(c)
            rect = (x,y), (ww,hh), angle = cv2.minAreaRect(c)
            area = ww*hh

            # if not not_center_bot(x):
            #     continue

            if isVertical(x) or isHorizon(y):
                continue
            if hh == 0:
                continue
            if ww > hh:
                temp = hh
                hh = ww
                ww = temp
            rect_ratio = ww/hh
            # if rect_ratio > 0.7:
            #     continue
            if y > 450:
                continue
            if area < 500:
                continue
            if area_h < ww:
                area_h = ww
            if area_h < hh:
                area_h = hh
            # if x<width/2:
            #     left = 1
            #     cy += y
            #     count_h += 1
            # else:
            #     right = 1
            #     cy += y
            #     count_h += 1

            # if y > 320:
            #     continue
            x_lr = x
            count_h += 1
            cy += y
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            print('draw')
            cv2.drawContours(im_draw, [box], -1, (0, 0, 255,), 2) 
            cv2.drawContours(im_draw, c, -1, (0 , 255, 0), 2)
            cv2.circle(im_draw ,(int(x), int(y)), 5, (0, 0, 255), -1)
            verticalX = (x - offsetW)/offsetW
            verticalY = (offsetH - y)/offsetH
        if count_h != 0:
            cy /= count_h

        if count_h > 2:
            count_h = 2

        max = 0
        count_bot = 0
        for c in contours_bot:
            M = cv2.moments(c)
            rect = (x,y), (ww,hh), angle = cv2.minAreaRect(c)
            area = ww*hh
            if isVertical(x) or isHorizon(y):
                continue
            if not_center_bot(x):
                continue
            if area_w < ww:
                area_w = ww
            if area_w < hh:
                area_w = hh
            if area < 1500:
                continue
            # if y > 320:
            #     continue
            print(area)
            # if max<area :
            #     max = area
            x_bot = x
            cx += x_bot
            count_bot += 1
                
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            # print('draw')
            cv2.drawContours(im_draw, [box], -1, (0, 0, 255,), 2) 
            cv2.drawContours(im_draw, c, -1, (0 , 255, 0), 2)
            cv2.circle(im_draw ,(int(x_bot), int(y)), 5, (0, 0, 255), -1)

        if count_bot != 0:
            cx /= count_bot

        if count_h == 1:
            if x_bot > x_lr:
                left = 1
                right = 0
            else:
                right = 1
                left = 0
        
        lpr = left + right
        if lpr == 1:
            if left == 1:      
                direction = -1
            else:
                direction = 1
        
        
        if count_h != 0 and area_w != 0:
            area = area_h*area_w
        ratio_area = area/im_size
        if cx != 0:
            cv2.circle(im_draw ,(int(cx), int(cy)), 5, (0, 0, 255), -1)
        cx = (cx-offsetW)/offsetW
        cy = (offsetH-cy)/offsetH
        print('cx',cx)
        print('cy',cy)
        print('direction',direction)
        print('ratio_area',ratio_area)
        print('left+right',left+right)
        cv2.imshow('im_draw', im_draw)
        cv2.waitkey(1)
        res.cx = cx
        res.cy = cy
        res.direction = direction
        res.ratioArea = ratio_area
        res.numVertical = count_h
        res.angle = -999
        res.appear = False
        return res

def navigate_bot():
    global img_bot, height_bot, width_bot
    while not rospy.is_shutdown():
        while img_bot is None:
            print('None')
        res = vision_msg_navigate()
        angle = -999
        appear = False
        im_bot = img_bot.copy()
        lower_yellow, upper_yellow = getColor('yellow', 'down')
        hsv = cv2.cvtColor(im_bot.copy(), cv2.COLOR_BGR2HSV)
        im_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
        im_yellow = close(im_yellow, rect_ker(5,5))

        _, contours, hierarchy = cv2.findContours(im_yellow.copy(), 
                                            cv2.RETR_TREE, 
                                            cv2.CHAIN_APPROX_SIMPLE)
        max_area = 0

        for c in contours:
            M = cv2.moments(c)
            rect = (x,y),(ww,hh),angle1 =cv2.minAreaRect(c)
            area = ww*hh
            if area < 1000:
                continue

            if max_area<area:
                max_area = area
                angle = Oreintation(M)[0]*180/math.pi 

        if max_area > 0:
            appear = True
        # else:
        #     appear = False
        if angle > 90:
            angle -= 180
        print('appear', appear)
        print('angle', angle)
        res.cx = -999
        res.cy = -999
        res.direction = -999
        res.ratioArea = -999
        res.numVertical = -999
        res.angle = -angle
        res.appear = appear
        return res


def img_callback(msg):
    global img

    arr = np.fromstring( msg.data, np.uint8)
    img = cv2.resize(cv2.imdecode(arr, 1), (640, 512))

def img_bot_callback(msg):
    global img_bot, height_bot, width_bot
    arr = np.fromstring( msg.data, np.uint8)
    img_bot = cv2.resize(cv2.imdecode(arr, 1), (640, 512))
    height_bot, width_bot,_ = img_bot.shape

def mission_callback(msg):
    print(msg.req.data)
    if msg.req.data == 'top':
        return navigate_top()
    if msg.req.data == 'bot':
        return navigate_bot()

if __name__ == '__main__':
    rospy.init_node('Navigate')
    bot = '/bottom/left/image_raw/compressed'
    top = '/top/center/image_rect_color/compressed'
    bag = '/rightcam_top/image_raw/compressed'
    rospy.Subscriber(bag, CompressedImage, img_callback)
    rospy.Subscriber(bot, CompressedImage, img_bot_callback)
    rospy.Service('vision_navigate', vision_srv_navigate(), mission_callback)
    rospy.spin()
    # navigate()
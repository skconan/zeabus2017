#!/usr/bin/env python
import rospy
from auto_exposure import AutoExposure
import constant as CONST


def main():
    EVmin = CONST.EV_TOP_MIN
    EVdefault = CONST.EV_TOP_DEFAULT

    subTopicC = rospy.get_param(
        "/auto_exposure_top/imageTopicC", None)
    clientC = rospy.get_param(
        "/auto_exposure_top/imageClientC", None)

    if not subTopicC is None:
        AEC = AutoExposure(subTopicC, clientC, CONST.IMAGE_TOP_WIDTH,
                           CONST.IMAGE_TOP_HEIGHT, EVdefault, EVmin)
        AEC.adjust_exposure_time()

if __name__ == '__main__':
    rospy.init_node('Auto_Exposure_Top')
    main()

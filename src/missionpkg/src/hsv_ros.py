
#! /usr/bin/env python

import roslib
import rospy
import cv2
import sys, time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ellipse_detection:

    def __init__(self):
        cv2.namedWindow('mywindow')
        cv2.namedWindow('thresh')
        
        cv2.createTrackbar('H High','thresh',0,255)
        cv2.createTrackbar('H Low','thresh',0,255)
        cv2.createTrackbar('S High','thresh',0,255)
        cv2.createTrackbar('S Low','thresh',0,255)
        cv2.createTrackbar('V High','thresh',0,255)
        cv2.createTrackbar('V Low','thresh',0,255)


        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("usb_cam/image_raw",Image,self.callback)

    def callback(self,data):
        try:
            img = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)


        hL = cv2.getTrackbarPos('H Low','thresh')
        sL = cv2.getTrackbarPos('S Low','thresh')
        vL = cv2.getTrackbarPos('V Low','thresh')
        hH = cv2.getTrackbarPos('H High','thresh')
        sH = cv2.getTrackbarPos('S High','thresh')
        vH = cv2.getTrackbarPos('V High','thresh')
        
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([hL,sL,vL])
        upper_hsv = np.array([hH,sH,vH])
        mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

        threshim = mask
        cv2.imshow('thresh', threshim)# remove this line(we don't need to show the output)
        cv2.imshow('mywindow', img)# remove this line(we don't need to show the output)
        cv2.waitKey(1)


def main(args):
    ed = ellipse_detection()
    rospy.init_node('ellipse_detection', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down ellipse_detection")
    cv2.destroyAllWindows()

if __name__ == '__main__':
main(sys.argv)

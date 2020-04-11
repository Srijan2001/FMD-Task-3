#!/usr/bin/env python
import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np

face_cascade=cv2.CascadeClassifier("/home/srijan/catkin_ws/src/task3/haarcascade_frontalface_default.xml")	#Path to XML file of classifier
bridge=CvBridge()
cap=cv2.VideoCapture("/home/srijan/Downloads/opencv-master/samples/data/Face_Detect.mp4")

def callback(data):
	data_ros=bridge.imgmsg_to_cv2(data,desired_encoding="passthrough")		
	_,frame=cap.read()		
	
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)			
	faces=face_cascade.detectMultiScale(gray,1.1,4)			



        for (x, y, w, h) in faces:     						#Cropping the image
	    r = max(w, h) / 2
            centerx = x + w / 2
            centery = y + h / 2
            nx = int(centerx - r)
            ny = int(centery - r)
            nr = int(r * 2)

            cropped = data_ros[ny:ny+nr, nx:nx+nr]

						
	cv2.namedWindow('frame',cv2.WINDOW_NORMAL)				#For resizing the output window
	cv2.resizeWindow('frame', 100,100)
			
	cv2.imshow('frame',cropped)
	
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
	

def listener():
	rospy.init_node("Node2",anonymous=True)
	rospy.Subscriber("/image_raw",Image,callback)	
	rospy.Subscriber("/image_raw",Image,callback)
	rospy.loginfo("Subscriber is starting")		
	rospy.spin()

if __name__=='__main__':
	listener()

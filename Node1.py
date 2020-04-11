#!/usr/bin/env python
import cv2
import numpy as np
import rospy
from cv_bridge import CvBridge,CvBridgeError
from sensor_msgs.msg import Image

face_cascade=cv2.CascadeClassifier("/home/srijan/catkin_ws/src/task3/haarcascade_frontalface_default.xml")	#Path to XML file of classifier
bridge=CvBridge()
cap=cv2.VideoCapture("/home/srijan/Downloads/opencv-master/samples/data/Face_Detect.mp4")			#Path to sample video

rospy.init_node("Node1",anonymous=True)
pub=rospy.Publisher("/image_raw",Image,queue_size=10)
rate=rospy.Rate(10)
rospy.loginfo("Publisher is starting")

while cap.isOpened():
	_,frame=cap.read()
		
	
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)			#Converting the image to gray scale for the classifier
	
	faces=face_cascade.detectMultiScale(gray,1.1,4)			#Detecting the faces

	for (x,y,w,h) in faces:						
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)	#Applying rectangle to the faces	
	
	image_ros=bridge.cv2_to_imgmsg(frame,encoding="passthrough")
	pub.publish(image_ros)
	rate.sleep()
				
	
cap.release()
	


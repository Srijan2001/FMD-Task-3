# FMD-Task-3
Facial Detection using Haar Cascade 

In this project I have created 2 ROS nodes. The first one extracts the feed from a sample video file by an Image Subscriber. Facial detection is then implemented on the subscribed feed using Haar Cascade and OpenCV. The frames with detected faces are then published to the second ROS node, which crops the bounding box (detected face) from the Image subscribed.

# FMD-Task-3
Facial Detection using Haar Cascade 

Created 2 ROS nodes, the first one extracts the feed from a sample video file by an Image Subscriber. Facial detection is implemented on the sunscribed feed using Haar Cascade and OpenCV. The frames with detected faces are then published to the second ROS node, which crops the bounding box (detected face) from the Image subscribed.

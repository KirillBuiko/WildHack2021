import cv2 as cv
from windowCapture import WindowCapture
from time import time
import os
import numpy as np
from vision import Vision

wincap = WindowCapture('test.py - WildHack - Visual Studio Code')

vision_limestone = Vision(None)

cascade_limestone = cv.CascadeClassifier('cascade2/cascade.xml')

loop_time = time()

#screenshot = cv.imread('positive/DJI_0082.JPG')

while(True):

	screenshot = wincap.get_screenshot()
	# do object detection
	rectangles = cascade_limestone.detectMultiScale(screenshot)
	# draw the detection results onto the original image
	detection_image = vision_limestone.draw_rectangles(screenshot, rectangles)
	# display the images
	cv.imshow('Matches', detection_image)
	cv.waitKey()
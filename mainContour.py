# This script implements Active contours for 2D image

# import Needed packages
import cv2
import argparse
#import numpy as np
#import matplotlib.pyplot as plt
#from mpldatacursor import datacursor
# Function that loads the target 10 images
# 1st five are low degree tumor 
# 2nd  five are hight degree tumor
def loadimages():
	# initialize empty stacks
	colorimgStack , greyimgStack = [] ,[]
	# create reading path
	#mainpath = ""
	targetimgsNames = ["ball.jpg","pen.jpg"]
	for i in targetimgsNames:
		tempimg = cv2.imread(i)
		greytemp = cv2.cvtColor(tempimg,cv2.COLOR_BGR2GRAY)
		# append read images
		colorimgStack.append(tempimg)
		greyimgStack.append(greytemp)
		# Test it loaded or not by showing (Works)
		#cv2.imshow("colred img" , tempimg)
		#cv2.imshow("grey img" , greytemp)
		#cv2.waitKey(0)
		# !!!! NOT working !!!
		# Helper link
		#  http://stackoverflow.com/questions/27704490/interactive-pixel-information-of-an-image-in-python
		#fig, ax = plt.subplots()
		#ax.imshow(tempimg, interpolation='none')
		#datacursor(hover=True, bbox=dict(alpha=1, fc='w'))
		#plt.show()
	#return loaded imgs
	return colorimgStack , greyimgStack
# function that initialized the contour manually 
def initContour():
	# initialize empty list of lists
	# each cell have list of 2 cells [x-coords ,y-coords]
	icontour = []

	# return initial contour
	return icontour
# Trial function for selecting area then cropping
def crop(img):
	# initialize the list of reference points and boolean indicating
	# whether cropping is being performed or not
	refPt = []
	cropping = False 
	click_and_crop()
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False
		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)

# main function for active contours
def main():
	# Load target images
	colorimgStack , greyimgStack = loadimages()
	# initialize contour
	baseContour = initContour()
main() 
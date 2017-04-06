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

# main function for active contours
def main():
	# Load target images
	colorimgStack , greyimgStack = loadimages()
	# initialize contour
	baseContour = initContour()
main() 
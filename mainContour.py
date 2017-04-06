# This script implements Active contours for 2D image

# import Needed packages
import cv2
import argparse
import matplotlib.pyplot as plt
# Function that loads the target 10 images
def loadimages():
	# 1st five are low degree tumor 
	# 2nd  five are hight degree tumor
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
# Class for contour initiation per image   
class Contour():
    def __init__(self , targetimage):
        self.img = targetimage
        self.point = []

    def getCoord(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.imshow(self.img)
        cid = fig.canvas.mpl_connect('button_press_event', self.__onclick__)
        plt.show()
        return self.point

    def __onclick__(self,click):
        currntClick = (click.xdata,click.ydata)
        centerx = int(currntClick[0])
        centery = int(currntClick[1])
        self.point.append((centerx,centery))
        #print self.point
        return self.point
# function that created objs of countour per image
def objCreation(imgList):
	objList = []
	# have ERROR dont know why !!
	for i in imgList:
		objList.append(Contour(i))
		#print ("obj list lenght : ", len(objList))
	return objList
# Function Draw contours 
def drawcontour(im , contourPoints):
	# input :
	# -------
	# img : target image need to draw ower it the points
	# points : list of positions where contour is
	# output :
	# -------
	# Displaied image with contour
	# Helper link
	# https://pythonprogramming.net/drawing-writing-python-opencv-tutorial/
    for i in contourPoints:
        cv2.circle(im, i, 3 , (255,255,255), thickness=3)
    cv2.imshow("initial contour" , im)
    #cv2.imwrite("init-{0}.png".format(i),im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return im
# function that initialized the contour manually 
def initContour(imgList):
	# initialize empty list of lists
	# each cell have list of 2 cells [x-coords ,y-coords]
	icontours = []
	TargetObjs =[]
	TargetObjs = objCreation(imgList)
	for i,currObj in enumerate(TargetObjs):
		# initialive contour
		currContour = currObj.getCoord()
		icontours.append(currContour)
		# draw contour initialized
		imgwithContour = drawcontour(imgList[i],currContour)
		# save image with contour
		cv2.imwrite("init-{0}.png".format(i),imgwithContour)
		# it works with 1st image only !! dont know why !!!
		break
	# return initial contour
	return icontours
# function that saves contour points in text file
def saveContourPoints(points):
	# open file
	f = open('init-0.txt', 'w')
	# loop on points
	for p in points:
		# get current coords
		x = p[0]
		y = p[1] 
		# write in file the current point
		# Newline
		f.write('{0} {1} \n'.format(x,y))
	# close file

# main function for active contours
def main():
	# Load target images
	colorimgStack , greyimgStack = loadimages()
	# initialize contour
	baseContours = initContour(colorimgStack)
	# Save contours in text file
	saveContourPoints(baseContours[0])
main() 
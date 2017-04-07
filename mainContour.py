# This script implements Active contours for 2D image
# import Needed packages
import cv2
import math
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
	f.close()
# function that loads the contour points from text 
def loadinitContour(fileName):
	conPoints = []
	# openfile
	f = open(fileName, 'r')
	# read line by line 
	content = [x.strip('\n') for x in f.readlines()]
	# split x, y
	for i ,line in enumerate(content):
		x,y = line.split()      
		#print ("x{0}:".format(i) , x)
		#print ("y{0}:".format(i) , y)
		conPoints.append((int(x),int(y)))
	# append points
	# close file
	f.close()
	#print ("lenght of contour :" , len(conPoints))
	return conPoints
# Function that calculates the internal energy
def getinternalEnergy(c , a , b):
	# Inputs : 
	#---------
	# c : contour points
	# a : alpha ( Elasticity coeffecient ) [should be small to be more elastic]
	# b : beta ( Curveture coeffcient )
	# ===============
	# output:
	#--------
	# total energy : list of Total Internal energy on each point
	#======================
	#======================
	totalEnergy = []
	# v_last : contour point before current point 
	# v_curr : contour current point
	# v_next : contour point after current point
	# Loop on contour points
	for i in range(len(c)):
		# get current inportant values
		if(i==0):
			v_last = c[-1] # make previouse one is the last one
			v_curr = c[i]
			v_next = c[i+1]
		elif (i == (len(c)-1)):
			v_last = c[i-1]
			v_curr = c[i]
			v_next = c[0] # make next one equal 1st one
		else:
			v_last = c[i-1]
			v_curr = c[i]
			v_next = c[i+1]
		#print ("v_last :", v_last)
		#print ("v_curr :", v_curr)
		#print ("v_next :", v_next)
		#---------------------------
		# get 1st drivative
		firstDrivX = v_next[0] - v_curr[0]
		firstDrivY = v_next[1] - v_curr[1]
		firstDriv = (firstDrivX , firstDrivY)
		#print ("First Drivative :", firstDriv)
		firstDrivPowerX = math.pow(firstDriv[0] ,2)
		firstDrivPowerY = math.pow(firstDriv[1] ,2)
		firstDrivPower = (firstDrivPowerX , firstDrivPowerY)
		#print ("First Drivative power 2 :", firstDrivPower)
		# ----------------------------------
		# Calculate elasticity / stiffness
		eX = a * firstDrivPower[0]
		eY = a * firstDrivPower[1]
		elasticity = (eX , eY)
		#print ("Elasticity :", elasticity)
		# ---------------------------------
		# ========================================
		####	CLACLULATE 2nd Drivative 	####
		#-----------------------------------
		secDrivX = v_next[0] - (2 * v_curr[0]) + v_last[0]
		secDrivY = v_next[1] - (2 * v_curr[1]) + v_last[1]
		secDriv = (secDrivX , secDrivY)
		#print("Secound Drivative :" ,secDriv)
		secDrivPowerX = math.pow(secDriv[0] ,2)
		secDrivPowerY = math.pow(secDriv[1] ,2)
		secDrivPower = (secDrivPowerX , secDrivPowerY)
		#print ("Secound Drivative power 2 :", secDrivPower)
		# ----------------------------------
		# Calculate curvature
		curX = b * secDrivPower[0]
		curY = b * secDrivPower[1]
		curvature = (eX , eY)
		#print ("Curvature :", curvature)
		# ---------------------------------
		# ========================================
		####	CLACLULATE Total Energy 	####
		#-----------------------------------
		eTotalX = elasticity[0] + curvature[0]
		eTotalY = elasticity[1] + curvature[1]
		eTotal = (eTotalX , eTotalY)
		#print ("Total Energy of point {0}:".format(i) , eTotal)
		totalEnergy.append(eTotal)
	# return total every list calculated
	return totalEnergy
# function that calculated the image energy (external energy)
def getExternalEnergy(img):
	# Input :
	#--------
	# img : is grey scale image that need to calculate its energy
	# ==============
	# output :
	# --------
	# matrix == image size : represents energy value at each position pixel
	#================================================
	# lets calculate gradient in X direction 
	# using soble filter in x direction
	







	
# main function for active contours
def main():
	# Load target images
	colorimgStack , greyimgStack = loadimages()
	print ("Images loaded : DONE")
	# initialize contour
	#baseContours = initContour(colorimgStack)
	# Save contours in text file
	#saveContourPoints(baseContours[0])
	# Load initial contours
	ballcontour = loadinitContour('init-0.txt')
	pencontour = loadinitContour('init-1.txt')
	print("Initial contour points loaded from file : DONE")
	####	CALCULATE ENERGYIES	 #### 
	alpha = 0.3 # Elasticity coeffecient
	beta = 0.1 # Curveture coeffcient
	# Calculate internal energy 
	ball_InternalEnergy = getinternalEnergy(ballcontour,alpha, beta)
	pen_InternalEnergy = getinternalEnergy(pencontour,alpha, beta)
	print ("Calculate internal Energy of contour : DONE")
	# ---------------------------------
	# Calculate External Energy (Image energy)
	ball_ExternalEnergy = getExternalEnergy(greyimgStack[0])  
main() 
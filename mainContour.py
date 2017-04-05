# This script implements Active contours for 2D image

# import Needed packages

# Function that loads the target 10 images
# 1st five are low degree tumor 
# 2nd  five are hight degree tumor
def loadimages():
	# initialize empty stacks
	colorimgStack , greyimgStack = []
	# create reading path
	mainpath = ""
	targetimgsNames = ["",""]
	for i in targetimgsNames:
		tempimg = cv2.imread(mainpath+i)
		greytemp = cv2.cvtColor(tempimg,cv2.COLOR_BGR2GRAY)
		# append read images
		colorimgStack.append(tempimg)
		greyimgStack.append(greytemp)
		cv.show("colred img" , tempimg)
		cv.show("grey img" , greytemp)
	#return loaded imgs
	return colorimgStack , greyimgStack

# main function for active contours
def main():
 	# Load target images
 	colorimgStack , greyimgStack = loadimages()

 main() 
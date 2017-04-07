# ActiveContour2D
This repository implements greedy active contour 2D 

# Main Steps
- load the target images 
	* convert them to grey scale
	* keep them in rgb and gray scale
- Initialize contour 
	* make class contour to get position coords on mouse click on image
	* draw contours selected on the target image
	* draw lines between contour points
	* save the image with contours
	* save contour points in text file same name as its image with contour
	* load initial contour points points directly from text file
- Calculate Internal Energy
	* calculate 1st drivative and get Elasticity factor (Using alpha coefficient)
	* calculate 2nd drivative and get Curvature factor (Using beta coefficient)
	* calculate total internal energy at each point (Using Elasticity & Curvature)
- Calculate External Energy
	* Calculate gradient in x and y direction of image using Sobel filter
	- (Helper link)
		* http://stackoverflow.com/questions/7185655/applying-the-sobel-filter-using-scipy
	- save image after edge detection.










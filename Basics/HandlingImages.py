import cv2
import numpy as np

def main():
	
	# reading the image
	image = cv2.imread('TestImages/peppers_color.tif',0)
	# Displaying the image
	cv2.imshow('Doremon',image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

main()
import cv2
import numpy as np

def main():
	
	# reading the image
	image = cv2.imread('Images/ImageSet-2/lena_color_256.tif',1)
	# Displaying the image
	cv2.imshow('Lena',image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

main()
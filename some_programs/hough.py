import sys
import cv2 as cv
import numpy as np
import time
def main(argv):
	en = time.time()
	default_file = 'hough_cd.jpg'
	filename = argv[0] if len(argv) > 0 else default_file
	# Loads an image
	# src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
	src = cv.imread(filename, cv.IMREAD_COLOR)
	img = np.copy(src)
	# Check if image is loaded fine
	if src is None:
		print ('Error opening image!')
		print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
		return -1
	
	
	gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
	
	
	gray = cv.medianBlur(gray, 5)
	
	
	rows = gray.shape[0]
	circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
							   param1=100, param2=30,
							   minRadius=1, maxRadius=1000)
	
	# print(len(circles))		# 3 tane print 0.005 - 0.0010 arası süre farkı oluşturuyo nasılsa
	# print(type(circles[0]))	# ama emin değilim
	if circles is not None:
		# print("algilamis")
		circles = np.uint16(np.around(circles))
		for i in circles[0, :]:
			center = (i[0], i[1])
			# circle center
			cv.circle(src, center, 1, (0, 100, 100), 3)
			# circle outline
			radius = i[2]
			cv.circle(src, center, radius, (255, 0, 255), 3)
	print('süre: ',time.time()-en)
	ikisi = np.hstack((src,img))
	cv.imshow("detected circles", ikisi)
	cv.waitKey(0)
	
	return 0
if __name__ == "__main__":
	main(sys.argv[1:])
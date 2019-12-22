import argparse
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", help = "the image that you wanna load")
args = vars(ap.parse_args())
image = cv2.imread(args["images"])
cv2.imshow("original",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_histogram= cv2.calcHist([gray_image], [0] , None , [256], [0,256] )
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(gray_histogram)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()



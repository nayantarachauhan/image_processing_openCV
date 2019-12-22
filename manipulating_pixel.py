import argparse
import numpy as np 
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Give the path of your image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("original", image)
cv2.waitKey(0)

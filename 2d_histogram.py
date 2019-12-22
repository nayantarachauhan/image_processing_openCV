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

chans = cv2.split(image)
colors = ("b", "g", "r")

fig = plt.figure()
ax = fig.add_subplot(111)
hist = cv2.calcHist([chans[0], chans[1]] , [0,1] , None , [32,32], [0,256,0,256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("b and g and 2d histogram")
plt.colorbar(p)
plt.show(p)

cv2.waitKey(0)
cv2.destroyAllWindows()

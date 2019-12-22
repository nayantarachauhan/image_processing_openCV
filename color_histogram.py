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
plt.figure()
plt.title("’Flattened’ Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
    






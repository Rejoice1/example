import numpy as 
import cv2
orb = cv2.ORB_create()
im =  cv2.imread('pp.jpeg', 0)
fast = cv2.FastFeatureDetector()
kpts = orb.detect(im)
print(kpts[0].pt)
(336.0, 13.0)

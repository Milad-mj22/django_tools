import imutils

import numpy as np
import cv2
im = np.random.rand(1920,1200)
cv2.imshow('a',im)
# cv2.waitKey(0)
import time
for i in range(1000):
    t1= time.time()

    im = imutils.rotate(image=im,angle=90)

    t2 =time.time()

    cv2.imshow('a',im)
    # cv2.waitKey(0)

    print(t2-t1)
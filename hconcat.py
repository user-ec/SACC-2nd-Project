import cv2 as cv
import numpy as np

for i in range(3001,4601):
    im_sk = cv.imread('/{}.png'.format(i))
    im_dk = cv.imread('/{}.png'.format(i))

    im_h=cv.hconcat([im_dk, im_sk])
    cv.imwrite('/{}.png'.format(i), im_h)

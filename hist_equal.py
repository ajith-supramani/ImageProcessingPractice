"""
.. module:: Histogram Equalization
   :platform: Windows
   :synopsis: This module does histogram equalization(Modifying contract) in input image

.. module author:: Ajith Supramani (ajithsupramani26595@gmail.com)
.. copyrights:  Ajith Supramani
.. date created: 30/09/2018

"""

import argparse
import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to input image")
    args = vars(ap.parse_args())

    # load the original image
    original = cv2.imread(args["image"], 0)

    # creating a Histograms Equalization
    # of a image using cv2.equalizeHist()
    equ = cv2.equalizeHist(original)

    # stacking images side-by-side and resize an image
    res = np.vstack((original, equ))
    res = cv2.resize(res, (960, 600))

    # show image input vs output
    cv2.imshow('image', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Histogram Check
    # plt.hist(original.ravel(), 256, [0, 256])
    # plt.show()
    # plt.hist(res.ravel(), 256, [0, 256])
    # plt.show()

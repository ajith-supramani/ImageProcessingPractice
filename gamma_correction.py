"""
.. module:: Gamma Correction
   :platform: Windows
   :synopsis: This module does gamma correction (light signal) in input image

.. module author:: Ajith Supramani (ajithsupramani26595@gmail.com)
.. copyrights:  Ajith Supramani
.. date created: 30/09/2018

"""

from __future__ import print_function
import numpy as np
import argparse
import cv2


def adjust_gamma(image, gamma_val=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    inv_gamma = 1.0 / gamma_val
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)


if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to input image")
    args = vars(ap.parse_args())

    # load the original image
    original = cv2.imread(args["image"])

    # loop over various values of gamma
    for gamma_value in np.arange(0.0, 3.5, 0.5):
        # ignore when gamma is 1 (there will be no change to the image)
        # if gamma_value == 1:
        #     continue

        # apply gamma correction and show the images
        gamma_value = gamma_value if gamma_value > 0 else 0.1
        adjusted = adjust_gamma(original, gamma_value)
        cv2.putText(adjusted, "g={}".format(gamma_value), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        res = np.vstack((original, adjusted))
        res = cv2.resize(res, (690, 690))
        cv2.imshow("Images", res)
        cv2.waitKey(0)

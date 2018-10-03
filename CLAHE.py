"""
.. module:: Contrast Limited Adaptive Histogram Equalization
   :platform: Windows
   :synopsis: This module does adaptive histogram equalization(Modifying contract) in input image

.. module author:: Ajith Supramani (ajithsupramani26595@gmail.com)
.. copyrights:  Ajith Supramani
.. date created: 30/09/2018

"""

import argparse
import cv2
import numpy as np


def enhance(image, clip_limit=3):
    # convert image to LAB color model
    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # split the image into L, A, and B channels
    l_channel, a_channel, b_channel = cv2.split(image_lab)

    # apply CLAHE to lightness channel
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(8, 8))
    cl = clahe.apply(l_channel)

    # merge the CLAHE enhanced L channel with the original A and B channel
    merged_channels = cv2.merge((cl, a_channel, b_channel))

    # convert iamge from LAB color model back to RGB color model
    final_image = cv2.cvtColor(merged_channels, cv2.COLOR_LAB2BGR)
    return final_image


if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to input image")
    ap.add_argument("-cl", "--clip_limit", required=False,
                    help="clip limit")
    args = vars(ap.parse_args())

    # load the original image
    original = cv2.imread(args["image"])

    # set the clip limit
    clip_lim = int(args["clip_limit"])

    output = enhance(original, clip_lim)

    # stacking images side-by-side and resize an image
    res = np.vstack((original, output))
    res = cv2.resize(res, (960, 600))

    # show image input vs output
    cv2.imshow('image', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


import cv2
import numpy as np

def stitch_images(img1, img2):
    stitch = np.zeros((max(img1.shape[0], img2.shape[0]), img1.shape[1] + img2.shape[1], 3), dtype=np.uint8)
    stitch[:img1.shape[0], :img1.shape[1], :] = img1
    stitch[:img2.shape[0], img1.shape[1]:, :] = img2

    return stitch[:min(img1.shape[0], img2.shape[0]), :, :]


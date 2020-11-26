import pafy
import cv2
import os
from matplotlib import pyplot as plt
import shutil
import numpy as np

class Conversation:

    def Invert(self, image):
        dst = cv2.bitwise_not(image)
        return dst


    def Gray(self, image):
        dst = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return dst


    def Blur(self, image):
        kernel = np.ones((2, 2), np.uint8)
        ChangedImage = cv2.filter2D(image, -1, kernel)
        return ChangedImage


    def Shrpen(self, image):

        dst0 = cv2.GaussianBlur(image, (5,5), 10,10)
        # 잡음을 제거한다.
        dst1 = cv2.medianBlur(dst0, ksize=11)
        # edge만 남기기
        kernel = np.array([[1,1,1],[1,-8,1],[1,1,1]])
        dst = cv2.filter2D(image, -1, kernel)

        dst2 = cv2.filter2D(dst1, -1, kernel)



import cv2
import numpy as np
from morphological_operator import binary

wait_key_time = 0

'''
hard code test
'''
img_test = np.zeros((5, 4), np.uint8)
img_test[0, 1] = 1
img_test[1, 0] = 1
img_test[1, 1] = 1
img_test[1, 2] = 1
img_test[2, 1] = 1
img_test[3, 1] = 1
img_test[4, 1] = 1


cv2.imshow('hard code test', img_test)

kernel_1 = np.zeros((1, 2), np.uint8)
kernel_1[0, 1] = 1
test_erode = cv2.erode(img_test, kernel_1, iterations=1)
test_dilate = cv2.dilate(img_test, kernel_1, iterations=1)
# cv2.imwrite('D:\\hard_code_test_original.png', img_test)
# cv2.waitKey(wait_key_time)

kernel_2 = np.ones((1, 2), np.uint8)
test_erode_2 = cv2.erode(img_test, kernel_2, iterations=1)
test_dilate_2 = cv2.dilate(img_test, kernel_2, iterations=1)

kernel_3 = np.zeros((2, 1), np.uint8)
kernel_3[1, 0] = 1
test_erode_3 = cv2.erode(img_test, kernel_3, iterations=1)
test_dilate_3 = cv2.dilate(img_test, kernel_3, iterations=1)

kernel_4 = np.ones((2, 1), np.uint8)
test_erode_4 = cv2.erode(img_test, kernel_4, iterations=1)
test_dilate_4 = cv2.dilate(img_test, kernel_4, iterations=1)

cv2.waitKey(wait_key_time)

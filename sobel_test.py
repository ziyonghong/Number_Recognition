import cv2
import matplotlib.pyplot as plt

import tensorflow as tf
import numpy as np

image = cv2.imread('./datasets/gray_wx_pic.jpg', cv2.IMREAD_GRAYSCALE)
# print(image)
image = np.array(image, np.float32)
image = np.reshape(image, [1, 3968, 2976, 1])
# cv2.imwrite('./datasets/gray_wx_pic.jpg', image)


w = np.array([
[-2, -1, 0], [-1, 0, 1], [0, 1, 2]

])
w = np.reshape(w, [3, 3, 1, 1])


conv = tf.nn.conv2d(image, w, [1, 1, 1, 1], 'SAME')

sess = tf.Session()

final = np.reshape(sess.run(conv), [3968, 2976])
cv2.imwrite('./datasets/conv.jpg', final)

import tensorflow as tf

sess = tf.Session()
saver = tf.train.import_meta_graph('model/LeNet.meta')
saver.restore(sess, './model/LeNet')

graph = tf.get_default_graph()
image_input = graph.get_tensor_by_name('INPUT/image_input:0')
softmax = graph.get_tensor_by_name('fully_connect_2/softmax:0')


import matplotlib.pyplot as plt

# 0: 没人，1: 有人
# w = graph.get_tensor_by_name('w:0')
# b = graph.get_tensor_by_name('b:0')

import read_data
import numpy as np

image_path, label_path = read_data.get_image_label_paths(48)
test_image, test_label = read_data.read_image_and_label(image_path, label_path)
print(len(test_image), len(test_label))
plt.figure(num=1, figsize=(7, 7))
for index in range(len(test_label)):
    plt.subplot(5, 5, index + 1)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel(test_label[index])
    plt.imshow(test_image[index])

plt.figure(num=2, figsize=(8, 8))
for index in range(len(test_label)):
    plt.subplot(5, 5, index + 1)
    plt.xticks([])
    plt.yticks([])
    reshaped = np.reshape(test_image[index], [1, 64, 64, 3])
    plt.xlabel("Recognize:" + str(np.argmax(sess.run(softmax, {image_input: reshaped}), 1)[0]))
    plt.imshow(test_image[index])
plt.show()

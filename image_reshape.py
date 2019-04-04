import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def read_data(imgpath='./datasets/library/lib_photo.png', labeltxt='./datasets/wenben/data1.txt'):
    lib_pic = cv.imread(imgpath)
    data = open(labeltxt, 'r')
    lines = data.readline().split(',')

    label_names = ['no', 'yes']
    labels = []
    positions = []
    x_starts = []
    y_starts = []
    x_ends = []
    y_ends = []
    for line in lines:
        words = line.split(' ')
        if len(words) < 6:
            break
        labels.append(int(words[0]))
        positions.append(int(words[1]))
        x_starts.append(int(words[2]))
        y_starts.append(int(words[3]))
        x_ends.append(int(words[4]))
        y_ends.append(int(words[5]))

    def get_labels():
        return labels

    def get_sub_images(photo=lib_pic):
        sub_images = []
        for index in range(0, len(labels)):
            img = photo[y_starts[index]: y_ends[index], x_starts[index]: x_ends[index]]
            img = cv.resize(img, (64, 64), interpolation=cv.INTER_CUBIC)
            b, g, r = cv.split(img)

            img2 = cv.merge([r, g, b])
            img2 = img2 / 255.0
            sub_images.append(img2)
        return sub_images

    return get_sub_images(), get_labels()


"""
plt.figure(figsize=(10, 10))
subs = get_sub_images()

for index in range(len(subs)):
    plt.subplot(6, 6, index + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)

    plt.imshow(subs[index])
    plt.xlabel(label_names[labels[index]])
print(labels[index], x_starts[index], y_starts[index], x_ends[index], y_ends[index])

img = lib_pic[y_starts[index]: y_ends[index], x_starts[index]: x_ends[index]]
print(img.shape)
img = cv.resize(img, (64, 64), interpolation=cv.INTER_LINEAR)
print(img.shape)

plt.imshow(img)
plt.show()
"""



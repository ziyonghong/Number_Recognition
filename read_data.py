import cv2
import matplotlib.pyplot as plt

image_path = './datasets/data/DATA53/image-53.png'
label_path = './datasets/data/DATA53/lable53.txt'
def read_image_and_label(image_path, label_path, w=64, h=64):
    image = cv2.imread(image_path)
    b, g, r = cv2.split(image)
    image = cv2.merge([r, g, b])

    label_str = open(label_path, 'r').readline().split(',')
    label = []
    positions = []
    x_start = []
    x_end = []
    y_start = []
    y_end = []
    for line in label_str:
        if line == '':
            continue
        info = line.split(' ')
        label.append(int(info[0]))
        positions.append(int(info[1]))
        x_start.append(int(info[2]))
        x_end.append(int(info[3]))
        y_start.append(int(info[4]))
        y_end.append(int(info[5]))
    # print(x_start[0], x_end[0], y_start[0], y_end[0])
    # print(x_start[20], x_end[20], y_start[20], y_end[20])
    # image = np.array(image)
    plt.figure(num=1, figsize=(8, 8))
    resized_image = []
    for index in range(len(label)):
        plt.subplot(5, 5, 1 + index)
        plt.xticks([])
        plt.yticks([])
        # print(x_start[index], x_end[index], y_start[index], y_end[index])
        # print(image[x_end[0]: x_start[0], y_end[0]: y_start[0]])
        # plt.imshow(image[x_end[index]: x_start[index], y_end[index]: y_start[index]])
        # print(image[x_end[index]: y_end[index], x_start[index]: y_start[index]].shape)
        # 注意下标：end start
        import math
        resized = cv2.resize(image[min(x_end[index],  y_end[index]): max(x_end[index],  y_end[index]),
                             min(x_start[index], y_start[index]): max(x_start[index], y_start[index])], (w, h),
                             interpolation=cv2.INTER_CUBIC)
        resized_image.append(resized)
        import numpy as np
        # print(np.array(resized).shape)
        plt.imshow(resized)
        plt.xlabel(label[index])
        # print('label', label[index])
    # plt.show()
    return resized_image, label


def show():
    plt.show()
# read_image_and_label(image_path, label_path)

def get_image_label_paths(index=0):
    image_path = './datasets/data/DATA'+str(index)+'/image-'+str(index)+'.png'
    label_path = './datasets/data/DATA'+str(index)+'/lable'+str(index)+'.txt'
    return image_path, label_path

def get_all():
    image_data = []
    label_data = []
    for index in range(1, 57):
        if index % 10 == 0:
            print('读取:', "%.2f" % (100 * index / 56.0))
        img_path, lbl_path = get_image_label_paths(index)
        images, labels = read_image_and_label(img_path, lbl_path)
        for image in images:
            image_data.append(image)
        for label in labels:
            label_data.append(label)

    import numpy as np
    # print(np.array(image_data[0: 100]).shape, np.array(image_data[101: len(image_data)]).shape)
    print('读取完成，大小：', len(label_data))

    return np.array(image_data), np.array(label_data)

# get_all()

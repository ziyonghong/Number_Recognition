import cv2
import matplotlib.pyplot as plt
from PIL import Image


#image_path = './datasets/wx_pic_cut.jpg'
image_path = './datasets/wx_pic_cut3.jpg'

origin = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
plt.subplot(2, 1, 1)
plt.imshow(origin)
ret, image = cv2.threshold(origin, 100, 255, cv2.THRESH_BINARY)  # 第一个数字是二值化的阈值，255就不要变了
plt.subplot(2, 1, 2)
plt.imshow(image)
plt.show()  # 这列可以查看二值化结果
# cv2.imwrite('./datasets/gray.jpg', image)
import numpy as np

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 15))
bigger = cv2.erode(image,kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 2))
smaller = cv2.dilate(bigger,kernel)


cv2.imwrite("./datasets/bigger.jpg",bigger)
cv2.imwrite("./datasets/smaller.jpg",smaller)

contours, hierarchy = cv2.findContours(smaller, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(origin, contours, -1, (0, 0, 255), 2)
offset = 15
def get_min_and_max(contour):
    mini = 100000
    mini_ret = (0, 0)
    for pt in contour:
        value = pt[0][0] + pt[0][1]
        if value < mini:
            mini_ret = (pt[0][0], pt[0][1])
            mini = value

    maxi = 0
    maxi_ret = (0, 0)
    for pt in contour:
        value = pt[0][0] + pt[0][1]
        if value > maxi:
            maxi_ret = (pt[0][0], pt[0][1])
            maxi = value

    mini_ret = (mini_ret[0] - offset, mini_ret[1] - offset)
    maxi_ret = (maxi_ret[0] + offset, maxi_ret[1] + offset)
    return mini_ret, maxi_ret
plt.figure(num=1, figsize=(8, 8))
index = -1
print(len(contours), len(hierarchy[0]))


def max_list(lt):
    temp = 0
    max_str = 0
    for i in lt:
        if lt.count(i) > temp:
            max_str = i
            temp = lt.count(i)
    return max_str

print(hierarchy[0][:,3])
parent = max_list(list(hierarchy[0][:,3]))
print(max_list(list(hierarchy[0][:,3])))
# 后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓
for contour in contours:
    index += 1
    mini, maxi = get_min_and_max(contour)
    if mini[0] < -offset/2 or mini[1] < -offset/2:
        continue
    if hierarchy[0][index][3] != parent:
        continue
    print(mini, maxi)
    # cv2.line(origin, mini, maxi, 233, 5)
    plt.subplot(20, 20, index + 1)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('')
    plt.imshow(smaller[mini[1]: maxi[1], mini[0]: maxi[0]])
# 所有结果都输出了

cv2.imshow("img", origin)
plt.show()
cv2.waitKey(0)


cv2.imshow('', image)
cv2.waitKey(0)

# 我思考下，应该是这个文件

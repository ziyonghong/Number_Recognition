import pytesseract
import cv2
import re
import matplotlib.pyplot as plt

path = './datasets/wx_pic.jpg'
base_path = 'D:\\Users\\Admin\\PycharmProjects\\new_tf_poj\\datasets\\'

def recognize_number(path):
    result = []
    text = pytesseract.image_to_string(cv2.imread(path), lang='eng')
    lines = text.split('\n')
    print('text: ', text)
    for line in lines:
        print(line)
        s = re.sub('[^0-9]+', '', line)
        if s == '':
            continue
        result.append(s)
    plt.imshow(cv2.imread(path))
    return result


def show():
    plt.show()


# cut_path = './datasets/wx_pic.jpg'
cut_path = base_path + 'wx_pic.jpg'
recognize_number(cut_path)
show()

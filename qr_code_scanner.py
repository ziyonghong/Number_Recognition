from pyzbar import pyzbar
import matplotlib.pyplot as plt
import cv2
# 得到图片
# image_path = './datasets/wx_pic.jpg'


def show_codes(image_path):
    code_data = []
    code_type = []

    image = cv2.imread(image_path)
    barcodes = pyzbar.decode(image)  # 识别二维码或条形码


    for barcode in barcodes:  # 遍历所有结果
        (x, y, w, h) = barcode.rect  # 得到矩形
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 画矩形
        barcodeData = barcode.data.decode()  # 解码信息
        code_data.append(barcodeData)
        barcodeType = barcode.type  # 类型
        code_type.append(barcodeType)

        text = "{}({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (0, 0, 255), 2)
        # 写上去
        # print("Found 类型：{} 信息：{}".format(barcodeType, barcodeData))
    # plt.figure(figsize=(15, 15))
    # plt.imshow(image)  # 显示
    # cv2.imread(image)
    # cv2.imshow('image', image)
    # cv2.waitKey(0)
    return code_data, code_type, image


# show_codes(image_path)
def show():
    print('show')

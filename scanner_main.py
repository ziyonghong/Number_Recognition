import qr_code_scanner
#import number_recogonize


if __name__ == '__main__':
    st = u'委会警务'.encode('utf-8').decode()
    print('st', st)

    path = './datasets/wx_pic.jpg'
    d, t, image = qr_code_scanner.show_codes(path)
    for i in range(len(d)):
        print('type:', t[i], 'contain:', d[i])
    qr_code_scanner.show()
    import cv2
    cv2.imwrite('./datasets/saved.png', image)
    # numbers = number_recogonize.recogonize_number(path)
    # for number in numbers:
    #     print('line:', number)

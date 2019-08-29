from PIL import Image
#截图图片中的一部分
im = Image.open("./datasets/wx_pic_cut.jpg")
# 图片的宽度和高度
img_size = im.size
print("图片宽度和高度分别是{}".format(img_size))
'''
裁剪：传入一个元组作为参数
元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
'''
# 截取图片中一块宽400和高300都是的
x = 650
y = 200
w = 400
h = 300
region = im.crop((x, y, x + w, y + h))
region.save("./datasets/wx_pic_cut3.jpg")

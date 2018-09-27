'''
你有一个目录，装了很多照片，
把他们的尺寸变成都不大于iphone5分辨率的大小
'''

from PIL import Image
import os

dir_path = r'images'

def changes(dir_path):

    for pic_path in os.listdir(dir_path):
        pic_name = os.path.join(dir_path, pic_path)
        if pic_name.endswith('.jpeg') or pic_name.endswith('.jpg'):
            with Image.open(pic_name) as img:
                w, h = img.size
                if w > 1136 or h > 640:
                    multiple = w / 1136.0 if (w / 1136.0) >= (h / 640.0) else h / 640.0
                    # 也可以使用img.resize(),但是该函数只接收整数，可方法缩小，thumbnail可以接受百分比
                    # 这里是对宽和高做了同等比例的缩放
                    img.thumbnail((w / multiple, h / multiple), Image.ANTIALIAS)
                    img.save("{}_changed.jpg".format(pic_name.split('.')[0]))
                else:
                    print("该图片无需改变大小")
                pass
            pass
        pass
    pass



if __name__ == '__main__':

    changes(dir_path)

    pass
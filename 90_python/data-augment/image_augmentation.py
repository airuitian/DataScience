import random
import numpy as np

from PIL import ImageOps, ImageFilter
# ImageOps 模块支持很多图像的操作
# ImageFilter 包含很多对图像的滤波操作


def mirror(img):
    """
    对输入图片进行镜像变换

    参数 img 输入的图像数据

    return: 镜像后的数据
    """

    return ImageOps.mirror(img)


def crop(img, per):
    """
    对输入的图片进行剪裁处理

    参数 img 输入的图像数据
    参数 per 剪裁的百分比

    return: 剪裁后图像
    """

    # 获得输入图片的宽与高
    img_width, img_height = img.size
    # 要保留的宽度
    crop_width = img_width * per
    # 要保留的高度
    crop_height = img_height * per
    # crop(upper_left_x,upper_left_y,lower_right_x,lower_right_y))
    return img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def rotate(img, r_from, r_end):
    """
    对输入的图片进行旋转处理，旋转范围是[r_from, r_end]

    参数 img 输入的图像数据
    参数 r_from 旋转角度的起始位置
    参数 r_end  旋转角度的终止位置

    return: 旋转后图像
    """

    degree = random.randint(r_from, r_end)
    
    return img.rotate(degree)


def blur_filter(img):
    """
    对输入的图片进行模糊化处理

    参数 img 输入的图像数据
    参数 r_from 旋转角度的起始位置
    参数 r_end  旋转角度的终止位置

    return: 模糊化的图片
    """

    return img.filter(ImageFilter.BLUR)


def detail_filter(img):
    """
    对输入图片使用细节滤镜

    参数 img 输入的图像数据

    return: 细节增强的图片
    """

    return img.filter(ImageFilter.DETAIL)

def eage_enhace(img):
    """
    对输入的图片进行边缘强化处理

    参数 img 输入的图像数据

    return: 旋转后图像
    """

    return img.filter(ImageFilter.EDGE_ENHANCE)

def smooth(img):
    """
    对输入的图片光滑处理
    
    参数 img 输入的图像数据

    return: 旋转后图像
    """

    return img.filter(ImageFilter.SMOOTH)
import os
import random
# argparse 是python中用来处理命令行参数的包
import argparse
import image_augmentation as ia

from PIL import Image, ImageOps


def parse_args():
    """
    解析输入的参数
    """

    # description 参数可以描述脚本参数的作用，默认为空
    parser = argparse.ArgumentParser(
        description = 'A Simple Image Data Augmentation Tool',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    # 两个-代表参数名称，一个-代表参数的别名
    # 例如--percent, -p
    # help 参数说明
    # type 参数类型
    # required 是否为必须参数， 如果不输入则报错
    # default 默认值

    # 输入图片的位置
    parser.add_argument('--input_dir', required = True, 
                        help = 'Directory containing images')
    # 增强后的图片位置
    parser.add_argument('--output_dir', required = True,
                        help = 'Directory for augmented images')
    # 输入数据集中，百分之多少的数据要被增强
    parser.add_argument('-p', '--percent', 
                        help = 'Percent of images need to be augment',
                        type = float, default = 1.0)
    # 要剪切图片的百分比
    parser.add_argument('--p_crop',
                        help = 'Percent to crop an image',
                        type = float, default = 1.0)
    # 旋转图片的角度的起始角度
    parser.add_argument('--r_from',
                        help = 'Rotate from',
                        type = float, default = 30)
    # 旋转图片的角度的结束角度
    parser.add_argument('--r_end',
                        help = 'Rote end',
                        type = float, default = 40)

    # parse_args()执行之前，所有添加命令行参数都不会生效
    args = parser.parse_args()
    # args + '.' + 参数名字可以获得输入的参数
    # rstrip删除字符串末尾指定的字符
    args.input_dir = args.input_dir.rstrip(os.sep)
    args.output_dir = args.output_dir.rstrip(os.sep)

    return args


def generate_image_list(args):
    """
    获得需要增强的数据列表

    @param argparse args 输入的参数

    @return list 需要增强的列表
    """

    # Get file names and file numbers
    filenames = os.listdir(args.input_dir)
    random.shuffle(filenames)
    # 增强原数据集中百分之args.percent
    augment_num = int(len(filenames) * args.percent)
    print('The number of which need to be augment {}\n'.format(augment_num))
    filenames = filenames[: augment_num]

    return filenames


def save_img(file_name, im, args):
    """
    保存增强后的图片

    @param string   file_name 保存后的文件名
    @param PIL      im        图像数据
    @param argparse args      输入的参数
    """

    output_filepath = os.sep.join([
        args.output_dir,
        '{}'.format(file_name)])
    im.save(output_filepath)


def augment_images(filelist, args):
    """
    增强数据

    @param list     filelist 需要增强的数据列表
    @param argparse args     输入的参数
    """

    for filename in filelist:
        # 获得文件的全路径
        file_path = args.input_dir + os.sep + filename
        # 打开图片
        img = Image.open(file_path)
        
        # 从后向前找到.的位置
        dot_pos = filename.rfind('.')
        # 获得文件名
        imgname = filename[: dot_pos]
        # 获得后缀名
        ext = filename[dot_pos: ]

        print('Augmenting {} ...'.format(filename))

        # Prefix of image name
        varied_imgname = '{}_'.format(imgname)

        # Mirror an image
        img_varied = ia.mirror(img)
        save_img(varied_imgname + 'm' + ext , img_varied, args)

        # Crop an image
        img_varied = ia.crop(img, args.p_crop)
        save_img(varied_imgname + 'c' + ext , img_varied, args)
        
        # Rotate an image
        img_varied = ia.rotate(img, args.r_from, args.r_end)
        save_img(varied_imgname + 'r' + ext , img_varied, args)
        
        # Blur an image
        img_varied = ia.blur_filter(img)
        save_img(varied_imgname + 'b' + ext , img_varied, args)
        
        # Detial fileter
        img_varied = ia.detail_filter(img)
        save_img(varied_imgname + 'd' + ext , img_varied, args)
        
        # Eage enhance
        img_varied = ia.eage_enhace(img)
        save_img(varied_imgname + 'd' + ext , img_varied, args)
        
        # Smooth
        img_varied = ia.smooth(img)
        save_img(varied_imgname + 's' + ext , img_varied, args)


def main():
    """
    Main Function
    """

    # 解析参数
    args = parse_args()
    # 如果输出的路径不存在，则创建输出路径
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    print('Starting image data augmentation for {}\n'.format(args.input_dir))

    file_list = generate_image_list(args)

    print('Data augmentation begin:')

    augment_images(file_list, args)

    print('\nDone!')


if __name__ == '__main__':
    main()
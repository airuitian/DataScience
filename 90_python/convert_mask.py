import numpy as np

from PIL import Image

# 打开图片
mask = Image.open('./img_1.png')
print(mask.size)

# 将mask转换为数组
mask_array = np.asarray(mask)
print(mask_array.shape)

# 查看数组中的元素
# flatten()可以将数组转换为1维数组
print(set(mask_array.flatten()))

# 新的mask
mask_new = np.where(mask_array == 1, 150, mask_array)

im = Image.fromarray(mask_new.reshape(705, 564))
im.save('./img_3.png')

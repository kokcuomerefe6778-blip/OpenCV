import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

yol = r'C:\Users\Ömer Efe\Desktop\a\yazılım\OpenCV\pupy.png'
pic = Image.open(yol)

plt.imshow(pic)


type(pic)

pic_arr= np.asarray(pic)
pic_arr.shape

plt.imshow(pic_arr)
pic_red = pic_arr.copy()

pic_red[:, :, 1] = 0
pic_red[:, :, 2] = 0

plt.imshow(pic_red)
plt.show()
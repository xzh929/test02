import PIL as pl
from PIL import Image
import numpy as np

image = Image.open('1.png')
# image.show()

image_array = np.array(image)
print(image_array.shape)
image_array2 = image_array.reshape(2, 540, 2, 960, 3)
image_array3 = image_array2.transpose(0, 2, 1, 3, 4)
image_array4 = image_array3.reshape(4, 540, 960, 3)

for i in range(4):
    img1 = Image.fromarray(image_array4[i])
    img1.show()


anti_image = image_array4.reshape(2,2,540,960,3)
print(anti_image.shape)
anti_image2 = anti_image.transpose(0,2,1,3,4)
anti_image3 = anti_image2.reshape(1080,1920,3)
img2 = Image.fromarray(anti_image3)
img2.show()


img_mid = image_array[360:720, 640:1280, :]
img3 = Image.fromarray(img_mid)
img3.show()

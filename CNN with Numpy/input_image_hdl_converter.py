import keras
import numpy as np
from keras.preprocessing import image
print('done')
def image_convert(directory):
    img = image.load_img(directory, target_size = (195,258),grayscale = False)
    img = image.img_to_array(img)
    img = img/255
    #put threshold to make it binary
    binarr = np.where(img>128, 255, 0)
    return binarr
if __name__ == '__main__':
    directory = r'C:\Users\user\Desktop\my research\CNN-on-FPGA-master\CNN-on-FPGA-master\CNN with Numpy\image reader\download.jpg'
    img = image_convert(directory)
    print(img)
    np.savetxt('array_image.MIF',img, delimiter = ',')
    print('done')
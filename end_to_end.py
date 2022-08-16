import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

IMGSIZE = (224, 224 ,3)
OUT_IMG_SIZE = (224 ,224 ,3)
target_size = [IMGSIZE[:2] ,OUT_IMG_SIZE[:2]]
paths = r"C:\Users\hp\anaconda\Project_files_Palmprint_detector\Test_Images"
def cos_mse(y_pred ,y_true):
    return 10*keras.losses.cosine_similarity(y_pred ,y_true) + 0.01*keras.losses.MeanSquaredError()(y_pred ,y_true)

stn_model = tf.keras.models.load_model('C:/Users/hp/anaconda/Project_files_Palmprint_detector/partial_model_step_5' , custom_objects ={'cos_mse' : cos_mse})
count = 1
img_arr = []
images_0 = os.listdir(paths)
for ind in range(len(images_0)):
    image_0 = images_0[ind]
    path_target_0 = f"{paths}\{image_0}"
    try:
        img_0 = img_to_array(load_img(path_target_0 , target_size = target_size[0])).astype(np.uint8)
    except:
        count = 3
        print('Failed at' + path_target_0 )
        print('Retrying ...')
        while count > 0:
            try:
                img_0 = img_to_array(load_img(path_target_0 , target_size = target_size[0])).astype(np.uint8)
                print('Error mitigated . Proceeding ...')
                break
            except:
                count -= 1
                if count == 0:
                    print('Failed to mitigate error . Skipping ...')
    if count == 0:
        continue
    img_arr.append(img_0)

img_arr = np.array(img_arr)
print(img_arr.shape)

im = stn_model(img_arr)    

for i in range(len(im)):
    tf.keras.preprocessing.image.array_to_img(im[0]).show()

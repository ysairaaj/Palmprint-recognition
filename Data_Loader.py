#import os
#import numpy as np
#import tensorflow as tf
#from tensorflow import keras
## Change the path directories here
Base_path = r"D:\BTP\4\IITD_Palmprint_V1"
##########################################

## instantiating lists for use later
## testing_code ##
print('Code started ...')
class data_loader:
    def __init__(self , Base_path = Base_path):

        self.left_hand = Base_path + r"\Left_Hand"
        self.right_hand = Base_path + r"\Right_Hand"
        self.left_segmented = Base_path + r"\Segmented\Left"
        self.right_segmented = Base_path + r"\Segmented\Right"
        self.left = [[] , []] #index 0 for input ,1 for target
        self.right =[[] , []]   #index 0 for input ,1 for target
        self.id = [[] , []] #index 0 for left_hand ,1 for right_hand

    def intersection(lst1, lst2):## O(n^2)
        lst1_0 = [x.split('.')[0] for x in lst1]
        lst2_0 = [x.split('.')[0] for x in lst2]
        lst3 = [value for value in lst1_0 if value in lst2_0]
        return [x + '.JPG' for x in lst3] , [x + '.bmp' for x in lst3]

    def auto_load(self , print_process = False ,show_examples = 5 ,ret =False , in_dim = (224,224) ,out_dim = (150,150) ):
        import os
        import numpy as np
        #import tensorflow as tf
        #from tensorflow import keras
        from tensorflow.keras.preprocessing.image import load_img
        from tensorflow.keras.preprocessing.image import img_to_array
        paths  = [[self.left_hand ,self.left_segmented ],[self.right_hand ,self.right_segmented]]
        text = ['left_hand' ,'right_hand']
        storage = [self.left , self.right , self.id ]
        target_size = [in_dim ,out_dim]
        for idx , paths in enumerate(paths):
            #print(idx ,path)
            counter = 0
            count = 1
            storage_target = storage[idx]
            id_target = self.id[idx]
            if print_process:
                print(f'processing {text[idx]} ...')

            images_0 = os.listdir(paths[0])
            #print(images_0[:5])
            images_1 = os.listdir(paths[1])
            images_0 , images_1= data_loader.intersection(images_0 ,images_1)
            #print(images_0)
            assert len(images_0) > 0 and len(images_1) > 0, f'Expected len(images_0) > 0 and len(images_1) > 0, got len(images_0) = {len(images_0)} , len(images_1) = {len(images_1)}'

            for ind in range(len(images_1)):
                image_0 = images_0[ind]
                image_1 = images_1[ind]
                assert  image_0.strip().split('.')[0] == image_1.strip().split('.')[0] , f'Expected image_0 = image_1 but got image_0 = {image_0} , image_1 = {image_1} instead.'
                path_target_0 = f"{paths[0]}\{image_0}"
                path_target_1 = f"{paths[1]}\{image_1}"
                try:
                    img_0 = img_to_array(load_img(path_target_0 , target_size = target_size[0])).astype(np.uint8)
                    img_1 = img_to_array(load_img(path_target_1 , target_size = target_size[1])).astype(np.uint8)

                except:
                    count = 3
                    print('Failed at' + path_target_0 + ' and ' + path_target_1)
                    print('Retrying ...')
                    while count > 0:
                        try:
                            img_0 = img_to_array(load_img(path_target_0 , target_size = target_size[0])).astype(np.uint8)
                            img_1 = img_to_array(load_img(path_target_1 , target_size = target_size[1])).astype(np.uint8)
                            print('Error mitigated . Proceeding ...')
                            break
                        except:
                            count -= 1
                            if count == 0:
                                print('Failed to mitigate error . Skipping ...')
                if count == 0:
                    continue
                storage_target[0].append(img_0)
                storage_target[1].append(img_1)
                id_target.append(image_0.strip().split('_')[0])
                if print_process and counter < show_examples :
                    counter+=1
                    print(image_0.strip())
        print(f'Data loaded successfully with {len(self.left[0])} left_hand samples and {len(self.right[0])} right_hand samples')
        if ret:
            return np.array(self.left[0]) ,np.array(self.left[1]) ,np.array(self.id[0]) ,np.array(self.right[0]) ,np.array(self.right[1]),np.array(self.id[1])

    def crop_load(self , print_process = False ,show_examples = 5 ,ret =False , in_dim = (224,224) ,out_dim = (150,150) ,crop_ratio = 0):##needs degugging
        import os
        import numpy as np
        #import tensorflow as tf
        #from tensorflow import keras
        from tensorflow.keras.preprocessing.image import load_img
        from tensorflow.keras.preprocessing.image import img_to_array
        paths  = [[self.left_hand ,self.left_segmented ],[self.right_hand ,self.right_segmented]]
        text = ['left_hand' ,'right_hand']
        storage = [self.left , self.right , self.id ]
        target_size = [in_dim ,out_dim]
        for idx , paths in enumerate(paths):
            #print(idx ,path)
            counter = 0
            count = 1
            storage_target = storage[idx]
            id_target = self.id[idx]
            if print_process:
                print(f'processing {text[idx]} ...')

            images_0 = os.listdir(paths[0])
            #print(images_0[:5])
            images_1 = os.listdir(paths[1])
            images_0 , images_1= data_loader.intersection(images_0 ,images_1)
            #print(images_0)
            assert len(images_0) > 0 and len(images_1) > 0, f'Expected len(images_0) > 0 and len(images_1) > 0, got len(images_0) = {len(images_0)} , len(images_1) = {len(images_1)}'

            for ind in range(len(images_1)):
                image_0 = images_0[ind]
                image_1 = images_1[ind]
                assert  image_0.strip().split('.')[0] == image_1.strip().split('.')[0] , f'Expected image_0 = image_1 but got image_0 = {image_0} , image_1 = {image_1} instead.'
                path_target_0 = f"{paths[0]}\{image_0}"
                path_target_1 = f"{paths[1]}\{image_1}"
                try:
                    img_0 = img_to_array(load_img(path_target_0 , target_size = (target_size[0][0] + int(crop_ratio*target_size[0][0]) , target_size[0][1] + int(crop_ratio*target_size[0][1])) ) ).astype(np.uint8)[int((crop_ratio*target_size[0][0])//2):int((crop_ratio*target_size[0][0])//2) + target_size[0][0] ,int((crop_ratio*target_size[0][1])//2):int((crop_ratio*target_size[0][1])//2) + target_size[0][1] ,:]
                    img_1 = img_to_array(load_img(path_target_1 , target_size = target_size[1])).astype(np.uint8)
                    #print((target_size[0][0] + int(crop_ratio*target_size[0][0]) , target_size[0][1] + int(crop_ratio*target_size[0][1])) , crop_ratio)
                except:
                    count = 3
                    print('Failed at' + path_target_0 + ' and ' + path_target_1)
                    print('Retrying ...')
                    while count > 0:
                        try:
                            img_0 = img_to_array(load_img(path_target_0 , target_size = (target_size[0] + crop_ratio*targetsize[0] , target_size[1] + crop_ratio*targetsize[1]) ) ).astype(np.uint8)[(crop_ratio*targetsize[0])//2:-(crop_ratio*targetsize[0])//2 ,(crop_ratio*targetsize[1])//2:-(crop_ratio*targetsize[1])//2]
                            img_1 = img_to_array(load_img(path_target_1 , target_size = target_size[1])).astype(np.uint8)
                            print('Error mitigated . Proceeding ...')
                            break
                        except:
                            count -= 1
                            if count == 0:
                                print('Failed to mitigate error . Skipping ...')
                if count == 0:
                    continue
                storage_target[0].append(img_0)
                storage_target[1].append(img_1)
                id_target.append(image_0.strip().split('_')[0])
                if print_process and counter < show_examples :
                    counter+=1
                    print(image_0.strip())
        print(f'Data loaded successfully with {len(self.left[0])} left_hand samples and {len(self.right[0])} right_hand samples')
        if ret:
            return np.array(self.left[0]) ,np.array(self.left[1]) ,np.array(self.id[0]) ,np.array(self.right[0]) ,np.array(self.right[1]),np.array(self.id[1])

    def __call__(self ,print_process = False ,show_examples = 5 ,ret =False , in_dim = (224,224) ,out_dim = (150,150) ,mode = 'auto_load',crop_ratio = 0): ## modes = auto_load , crop_load
        if mode == 'auto_load':
            return self.auto_load(print_process  ,show_examples  ,ret  , in_dim  ,out_dim  )
        elif mode == 'crop_load':
            return self.crop_load(print_process ,show_examples ,ret , in_dim  ,out_dim  ,crop_ratio )

    def build_data(self , merge_left_right =False):
        import numpy as np
        if merge_left_right :
            return np.vstack(( np.array(self.left[0]) ,np.array(self.right[0]))) , np.vstack((np.array(self.left[1]) ,np.array(self.right[1]))) ,np.vstack((np.array(self.id[0]),np.array(self.id[1])))
        else:
            return np.array(self.left[0]) ,np.array(self.left[1]) ,np.array(self.id[0]) ,np.array(self.right[0]) ,np.array(self.right[1]),np.array(self.id[1])
    def clear_data(self):
        self.left = [[] , []] #index 0 for input ,1 for target
        self.right =[[] , []]   #index 0 for input ,1 for target
        self.id = [[] , []] #index 0 for left_hand ,1 for right_hand
        print("Data_Loader is cleared .")
print('Code executed successfully')

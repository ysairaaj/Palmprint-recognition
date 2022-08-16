#import Data_Loader as DL
import tensorflow as tf
from tensorflow import keras

#IMGSIZE = (224, 224 ,3)
#OUT_IMG_SIZE = (224 ,224 ,3)
#data_loader = DL.data_loader(Base_path = r"D:\BTP\4\IITD_Palmprint_V1")
#X,y,Label,X2,y2,Label2 = data_loader.build_data()
#data_loader.clear_data()

class sample_generator(tf.keras.utils.Sequence):
    def __init__(self , X_data ,y_data,label,batch_size):
        self.x = X_data
        self.y = y_data
        self.label = Label
        self.batch_size = batch_size
    def __len__(self) :
        return int(np.ceil(len(self.x)*(len(self.x)-1) / float(self.batch_size)))
    def __getitem__(self,idx):
        batch_x = [None ,None]
        batch_y = [[] ,[]]
        print((idx//(len(self.x)-1) + (idx%(len(self.x)-1))*self.batch_size)%(len(self.x)-1) ,(idx//(len(self.x)-1) + (idx%(len(self.x)-1))*self.batch_size)%(len(self.x)-1) + self.batch_size)
        batch_x = [np.tile(self.x[idx//(len(self.x)-1)] ,(self.batch_size ,1,1,1)) , self.y[(idx//(len(self.x)-1) + (idx%(len(self.x)-1))*self.batch_size)%(len(self.x)-1) :(idx//(len(self.x)-1) + (idx%(len(self.x)-1))*self.batch_size)%(len(self.x)-1) + self.batch_size,...]]
        batch_y[0].extend([self.label.tolist()[idx//(len(self.x)-1)]]*(self.batch_size))
        #print([self.label.tolist()[idx//(len(self.x)-1)]]*(self.batch_size) )
        batch_y[1].extend(self.label[(idx//(len(self.x)-1) + (idx%(len(self.x)-1))*self.batch_size)%(len(self.x)-1) :(idx//(len(self.x)-1) + (idx%(len(self.x)-1))*self.batch_size)%(len(self.x)-1) + self.batch_size,...].tolist())
        #print(self.label[(idx//(len(self.x)-1) + (idx%(len(self.x)-1))*self.batch_size)%(len(self.x)-1) :(((idx//len(self.x)-1)) + (idx%(len(self.x)-1))*self.batch_size)%(len(self.x)-1) + self.batch_size,...].tolist())
        batch_y = zip(batch_y[0] ,batch_y[1])
        y_arr = [0  if y[0] != y[1] else 1 for y in batch_y]
        print(len(batch_x[0]) ,len(batch_x[1]),len(y_arr))
        return batch_x , np.array(y_arr)

# Palmprint-recognition
Uses Spatial transformation networks to process palmprint images and train Deep neural network for person identification .
Packages used ----
 - Tensorflow
 - Numpy

Uses the following architecture for Palmprint ROI extraction :
![Architecture](Palm_ROI_extractor_model.png) 

The code implements the following pictorial representation :
![Spatial_transform_net](config2.PNG)  

Some examples of ROI extraction by the trained network are :
![Ex:1](diagram2.png)  and ![Ex:2](diagram3.png)    

The system works by using VGG-16 net to generate the parameters of the affine transformation matrix given below : 

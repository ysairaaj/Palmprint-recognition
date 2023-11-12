# Palmprint-recognition
Uses Spatial transformation networks to process palmprint images and train Deep neural network for person identification .
Packages used ----
 - Tensorflow
 - Numpy

Uses the following architecture for Palmprint ROI extraction :

<img src="Palm_ROI_extractor_model.png" width="100" height="100">
The code implements the following pictorial representation :
![Spatial_transform_net](config2.PNG)  

Some examples of ROI extraction by the trained network are :
![Ex:1](diagram2.png)  and ![Ex:2](diagram3.png)    

The system works by using VGG-16 net to generate the parameters of the affine transformation matrix given below : 

 ![Affine matrix](affine_matrix.PNG) 

 This helps in different kinds of transformations like translation , scaling , rotations , bending etc . 
 
![Affine transformations](Affine.png)  

This helps in extracting information containing person identity which can be used to compare and differentiate between people .

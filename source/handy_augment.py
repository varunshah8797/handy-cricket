# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:09:34 2020

@author: User
"""

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img 
   
# Initialising the ImageDataGenerator class. 
# We will pass in the augmentation parameters in the constructor. 
datagen = ImageDataGenerator( 
        rotation_range = 30, 
        shear_range = 0.2, 
        zoom_range = 0.2, 
        horizontal_flip = True, 
        brightness_range = (0.5, 1.5)) 

from glob import glob
file= glob("*.jpg")

for j in file:
    # Loading a sample image  
    img = load_img(j)  
    # Converting the input sample image to an array 
    x = img_to_array(img) 
    # Reshaping the input image 
    x = x.reshape((1, ) + x.shape)  
       
    # Generating and saving n_img augmented samples 
    n_img=2
    # using the above defined parameters.  
    i = 0
    for batch in datagen.flow(x, batch_size = 1, 
                              save_to_dir ='preview',  
                              save_prefix =j[:-4], save_format ='jpg'): 
        i += 1
        if i > n_img: 
            break
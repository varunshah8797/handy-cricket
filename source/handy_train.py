# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:30:02 2020

@author: User
"""

import cv2
import numpy as np
from keras_squeezenet import SqueezeNet
from keras.utils import np_utils
from keras.optimizers import Adam
from keras.layers import Activation, Dropout, Convolution2D, GlobalAveragePooling2D
from keras.models import Sequential
import tensorflow as tf
import os

IMG_SAVE_PATH = 'image_data'

CLASS_MAP = {
    "1": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "10": 9,
    "None": 10
}

NUM_CLASSES = len(CLASS_MAP)

def mapper(label):
    return CLASS_MAP[label]

def get_model():
    model = Sequential([
        SqueezeNet(input_shape=(227,227,3),include_top=False),
        Dropout(0.7),
        Convolution2D(NUM_CLASSES,(1,1),padding='valid'),
        Activation('relu'),
        GlobalAveragePooling2D(),
        Activation('softmax')
    ])

    return model

dataset = []

for directory in os.listdir(IMG_SAVE_PATH):
    path = os.path.join(IMG_SAVE_PATH,directory)
    if not os.path.isdir(path):
        continue
    for item in os.listdir(path):
        if item.startswith("."):
            continue
        img = cv2.imread(os.path.join(path,item))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (227,227))
        dataset.append([img,directory])


data, labels = zip(*dataset)
labels = list(map(mapper, labels))

# one hot encoding of labels
labels = np_utils.to_categorical(labels)

# defining the model
model = get_model()
model.compile(
    optimizer=Adam(lr=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

#training the model
model.fit(np.array(data), np.array(labels), epochs=3)

#saving the model separately
model.save("handy_cricket.h5")
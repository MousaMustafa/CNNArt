# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:59:36 2018

@author: Jiahuan Yang
"""
import os.path
import scipy.io as sio
import numpy as np  # for algebraic operations, matrices
import keras
import keras.optimizers
from keras.models import Sequential, Model
from keras.layers import Input
from keras.layers.core import Dense, Activation, Flatten, Dropout, Lambda, Reshape
from keras.activations import relu, elu, softmax
from keras.layers.advanced_activations import LeakyReLU, PReLU
from keras.initializers import Constant
from keras.layers import concatenate, add
from keras.layers.convolutional import Conv3D, Conv2D, MaxPooling3D, MaxPooling2D, ZeroPadding3D
from keras.regularizers import l1_l2, l2
from keras.models import model_from_json, load_model
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau


def createModel(patchSize):
    l1_reg = 0
    l2_reg = 1e-6
    cnn = Sequential()

    """ conv1 """
    cnn.add(Conv2D(64,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   input_shape=(1, int(patchSize[0]), int(patchSize[0])),
                   name='conv1_1'
                   ))

    cnn.add(Conv2D(64,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv1_2'
                   ))

    cnn.add(MaxPooling2D(pool_size =(2, 2),
                         strides=(2, 2),
                         padding='same',
                         name='pool1'
                         ))

    """ conv2 """
    cnn.add(Conv2D(128,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv2_1'
                   ))

    cnn.add(Conv2D(128,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv2_2'
                   ))

    cnn.add(MaxPooling2D(pool_size=(2, 2),
                         strides=(2, 2),
                         padding='same',
                         name='pool2'
                         ))

    """ conv3 """
    cnn.add(Conv2D(256,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv3_1'
                   ))

    cnn.add(Conv2D(256,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv3_2'
                   ))

    cnn.add(Conv2D(256,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv3_3'
                   ))

    cnn.add(MaxPooling2D(pool_size=(2, 2),
                         strides=(2, 2),
                         padding='same',
                         name='pool3'
                         ))

    """ conv4 """
    cnn.add(Conv2D(512,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv4_1'
                   ))

    cnn.add(Conv2D(512,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv4_2'
                   ))

    cnn.add(Conv2D(512,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv4_3'
                   ))

    cnn.add(MaxPooling2D(pool_size=(2, 2),
                         strides=(2, 2),
                         padding='same',
                         name='pool4'
                         ))

    """ conv5 """
    cnn.add(Conv2D(512,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv5_1'
                   ))

    cnn.add(Conv2D(512,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv5_2'
                   ))

    cnn.add(Conv2D(512,
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1_reg, l2_reg),
                   strides=(1, 1),
                   activation='relu',
                   name='conv5_3'
                   ))

    cnn.add(MaxPooling2D(pool_size=(2, 2),
                         strides=(2, 2),
                         padding='same',
                         name='pool5'
                         ))

    cnn.add(Flatten(name='flatten'))
    cnn.add(Dense(units=2, kernel_initializer='he_normal', kernel_regularizer='l2', name='output'))
    cnn.add(Activation('softmax'))

    return cnn

def fTrain(X_train, y_train, X_test, y_test, sOutPath, patchSize, batchSizes=None, learningRates=None, iEpochs=None):
    # grid search on batch_sizes and learning rates
    # parse inputs
    batchSizes = [64] if batchSizes is None else batchSizes
    learningRates = [0.01] if learningRates is None else learningRates
    iEpochs = 300 if iEpochs is None else iEpochs

    # change the shape of the dataset
    X_train = np.expand_dims(X_train, axis=1)
    X_test = np.expand_dims(X_test, axis=1)
    y_train = np.asarray([y_train[:], np.abs(np.asarray(y_train[:], dtype=np.float32) - 1)]).T
    y_test = np.asarray([y_test[:], np.abs(np.asarray(y_test[:], dtype=np.float32) - 1)]).T

    for iBatch in batchSizes:
        for iLearn in learningRates:
            fTrainInner(X_train, y_train, X_test, y_test, sOutPath, patchSize, iBatch, iLearn, iEpochs)


def fTrainInner(X_train, y_train, X_test, y_test, sOutPath, patchSize, batchSize=None, learningRate=None, iEpochs=None):
    # parse inputs
    batchSize = [64] if batchSize is None else batchSize
    learningRate = [0.01] if learningRate is None else learningRate
    iEpochs = 300 if iEpochs is None else iEpochs

    print('Training 2D CNN')
    print('with lr = ' + str(learningRate) + ' , batchSize = ' + str(batchSize))

    # save names
    _, sPath = os.path.splitdrive(sOutPath)
    sPath, sFilename = os.path.split(sPath)
    sFilename, sExt = os.path.splitext(sFilename)
    model_name = sPath + '/' + sFilename + '/' + sFilename + '_lr_' + str(learningRate) + '_bs_' + str(batchSize)
    weight_name = model_name + '_weights.h5'
    model_json = model_name + '_json'
    model_all = model_name + '_model.h5'
    model_mat = model_name + '.mat'

    if (os.path.isfile(model_mat)):  # no training if output file exists
        return

    # create model
    cnn = createModel(patchSize)

    cnn.summary()

    # opti = SGD(lr=learningRate, momentum=1e-8, decay=0.1, nesterov=True);#Adag(lr=0.01, epsilon=1e-06)
    opti = keras.optimizers.Adam(lr=learningRate, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
    callbacks = [EarlyStopping(monitor='val_loss', patience=10, verbose=1)]
    callbacks.append(ModelCheckpoint(model_all, save_weights_only=False, monitor='val_acc', verbose=1, period=2, save_best_only=True))  # overrides the last checkpoint, its just for security
    callbacks.append(ReduceLROnPlateau(monitor='loss', factor=0.5, patience=5, min_lr=1e-4, verbose=1))

    cnn.compile(loss='categorical_crossentropy', optimizer=opti, metrics=['accuracy'])
    print(cnn.summary)

    cnn.fit(X_train,
            y_train,
            validation_data=[X_test, y_test],
            epochs=iEpochs,
            batch_size=batchSize,
            callbacks=callbacks,
            verbose=1)

    # save model
    # cnn.save_weights(weight_name, overwrite=True)
    cnn.save(model_all)  # keras > v0.7



def fPredict(X_test, y_test, model_name, sOutPath, patchSize, batchSize):
    # weight_name = sOutPath + '/' + model_name + '_weights.h5'
    # model_json = sOutPath + model_name + '_json'
    model_all = sOutPath + model_name + '_model.h5'

    # model = createModel(patchSize)
    # opti = keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
    # callbacks = [EarlyStopping(monitor='val_loss', patience=10, verbose=1)]
    #
    # model.compile(loss='categorical_crossentropy', optimizer=opti, metrics=['accuracy'])
    # model.load_weights(weight_name)

    # load complete model (including weights); keras > 0.7
    model = load_model(model_all)

    # assume artifact affected shall be tested!
    # y_test = np.ones((len(X_test),1))

    X_test = np.expand_dims(X_test, axis=1)
    y_test = np.asarray([y_test[:], np.abs(np.asarray(y_test[:], dtype=np.float32) - 1)]).T

    score_test, acc_test = model.evaluate(X_test, y_test, batch_size=batchSize)
    prob_pre = model.predict(X_test, batchSize, 1)

    # modelSave = model_name[:-5] + '_pred.mat'
    modelSave = sOutPath + '/' + model_name + '_pred.mat'
    sio.savemat(modelSave, {'prob_pre': prob_pre, 'score_test': score_test, 'acc_test': acc_test})

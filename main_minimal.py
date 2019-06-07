'''
Copyright: 2016-2019 Thomas Kuestner (thomas.kuestner@med.uni-tuebingen.de) under Apache2 license
@author: Thomas Kuestner
'''
# imports
import sys
import numpy as np                  # for algebraic operations, matrices
import h5py
import scipy.io as sio              # I/O
import os                      # operating system
import argparse
from utils.data import *
from utils.dlnetwork import *
import utils.Label as Label
import datetime
import yaml


def fParseConfig(sFile):
    # get config file
    with open(sFile, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    return cfg


def fArtDetection(data, dlnetwork, sMode):
    # set GPU
    os.environ["CUDA_VISIBLE_DEVICES"] = str(data.gpu_id)

    # get output vector for different classes
    classes = np.asarray(np.unique(data.Y_train, ), dtype=int)
    data.classMappings = Label.mapClassesToOutputVector(classes=classes, usingArtefacts=data.usingArtifacts,
                                                        usingBodyRegion=data.usingBodyRegions,
                                                        usingTWeightings=data.usingTWeighting)

    Y_train = []

    Y_validation = []

    Y_test = []

    data.Y_segMasks_train[data.Y_segMasks_train == 3] = 1
    data.Y_segMasks_train[data.Y_segMasks_train == 2] = 0

    data.Y_segMasks_test[data.Y_segMasks_test == 3] = 1
    data.Y_segMasks_test[data.Y_segMasks_test == 2] = 0

    ##########################
    ###########################
    # for generating patch labels

    y_labels_train = np.expand_dims(data.Y_segMasks_train, axis=-1)
    y_labels_train[y_labels_train == 0] = -1
    y_labels_train[y_labels_train == 1] = 1
    y_labels_train = np.sum(y_labels_train, axis=1)
    y_labels_train = np.sum(y_labels_train, axis=1)
    y_labels_train = np.sum(y_labels_train, axis=1)
    y_labels_train[y_labels_train >= 0] = 1
    y_labels_train[y_labels_train < 0] = 0
    for i in range(y_labels_train.shape[0]):
        Y_train.append([1, 0] if y_labels_train[i].all() == 0 else [0, 1])
    Y_train = np.asarray(Y_train)

    y_labels_test = np.expand_dims(data.Y_segMasks_test, axis=-1)
    y_labels_test[y_labels_test == 0] = -1
    y_labels_test[y_labels_test == 1] = 1
    y_labels_test = np.sum(y_labels_test, axis=1)
    y_labels_test = np.sum(y_labels_test, axis=1)
    y_labels_test = np.sum(y_labels_test, axis=1)
    y_labels_test[y_labels_test >= 0] = 1
    y_labels_test[y_labels_test < 0] = 0

    for i in range(y_labels_test.shape[0]):
        Y_test.append([1, 0] if y_labels_test[i].all() == 0 else [0, 1])
    Y_test = np.asarray(Y_test)

    # change the shape of the dataset -> at color channel -> here one for grey scale

    # Y_segMasks_train_foreground = np.expand_dims(data.Y_segMasks_train, axis=-1)
    # Y_segMasks_train_background = np.ones(Y_segMasks_train_foreground.shape) - Y_segMasks_train_foreground
    # data.Y_segMasks_train = np.concatenate((Y_segMasks_train_background, Y_segMasks_train_foreground),
    #                                        axis=-1)
    # data.Y_segMasks_train = np.sum(data.Y_segMasks_train, axis=-1)
    #
    # Y_segMasks_test_foreground = np.expand_dims(data.Y_segMasks_test, axis=-1)
    # Y_segMasks_test_background = np.ones(Y_segMasks_test_foreground.shape) - Y_segMasks_test_foreground
    # data.Y_segMasks_test = np.concatenate((Y_segMasks_test_background, Y_segMasks_test_foreground),
    #                                        axis=-1)
    # data.Y_segMasks_test = np.sum(data.Y_segMasks_test, axis=-1)

    if data.X_validation.size == 0 and data.Y_validation.size == 0:
        data.X_validation = 0
        data.Y_segMasks_validation = 0
        data.Y_validation = 0
        print("No Validation Dataset.")
    else:
        for i in range(data.Y_validation.shape[0]):
            Y_validation.append(data.classMappings[data.Y_validation[i]])
        Y_validation = np.asarray(Y_validation)
        data.Y_segMasks_validation[data.Y_segMasks_validation == 3] = 1
        data.Y_segMasks_validation[data.Y_segMasks_validation == 2] = 0



    ################################################################################################################
    # debug!
    # for i in range(data.X_train.shape[0]):
    #
    #     plt.subplot(141)
    #     plt.imshow(data.X_train[i, :, :, 4, 0])
    #
    #     plt.subplot(142)
    #     plt.imshow(data.Y_segMasks_train[i, :, :, 4, 0])
    #
    #     plt.subplot(143)
    #     plt.imshow(data.Y_segMasks_train[i, :, :, 4, 1])
    #
    #     #plt.subplot(144)
    #     #plt.imshow(data.Y_segMasks_train[i, :, :, 4, 2])
    #
    #     plt.show()
    #
    #     print(i)

    ###################################################################################################################

    # output folder
    data.outPutFolderDataPath = data.pathOutput + os.sep + dlnetwork.neuralNetworkModel + "_"
    if data.patchingMode == 'PATCHING_2D':
        data.outPutFolderDataPath += "2D" + "_" + str(data.patchSizeX) + "x" + str(data.patchSizeY)
    elif data.patchingMode == 'PATCHING_3D':
        data.outPutFolderDataPath += "3D" + "_" + str(data.patchSizeX) + "x" + str(data.patchSizeY) + \
                                     "x" + str(data.patchSizeZ)

    data.outPutFolderDataPath += "_" + datetime.datetime.today().strftime('%Y-%m-%d_%H-%M')

    if not os.path.exists(data.outPutFolderDataPath):
        os.makedirs(data.outPutFolderDataPath)

    if not os.path.exists(data.outPutFolderDataPath + os.sep + 'checkpoints'):
        os.makedirs(data.outPutFolderDataPath + os.sep + 'checkpoints')

    # summarize cnn and training
    data.create_cnn_training_summary(dlnetwork.neuralNetworkModel, data.outPutFolderDataPath)

    # segmentation FCN training
    # dynamic loading of corresponding model
    # TODO: case switch here for the different networks
    sModel = 'networks.FullyConvolutionalNetworks.motion.VResFCN_3D_Upsampling_final_Motion_Binary'
    cnnModel = __import__(sModel, globals(), locals(), ['fTrain', 'fPredict'],
                          0)  # dynamic module loading with specified functions and with absolute importing (level=0) -> work in both Python2 and Python3

    if sMode == 'training':
        if not data.usingSegmentationMasks:
            cnnModel.fTrain(X_train=data.X_train,
                            y_train=Y_train,
                            X_valid=data.X_validation,
                            y_valid=Y_validation,
                            X_test=data.X_test,
                            y_test=Y_test,
                            sOutPath=data.outPutFolderDataPath,
                            patchSize=[data.patchSizeX, data.patchSizeY, data.patchSizeZ],
                            batchSizes=dlnetwork.batchSize,
                            learningRates=dlnetwork.learningRate,
                            iEpochs=dlnetwork.epochs,
                            dlnetwork=dlnetwork)
        else:
            cnnModel.fTrain(X_train=data.X_train,
                            y_train=Y_train,
                            Y_segMasks_train=data.Y_segMasks_train,
                            X_valid=data.X_validation,
                            y_valid=Y_validation,
                            Y_segMasks_valid=data.Y_segMasks_validation,
                            X_test=data.X_test,
                            y_test=Y_test,
                            Y_segMasks_test=data.Y_segMasks_test,
                            sOutPath=data.outPutFolderDataPath,
                            patchSize=[data.patchSizeX, data.patchSizeY, data.patchSizeZ],
                            batchSizes=dlnetwork.batchSize,
                            learningRates=dlnetwork.learningRate,
                            iEpochs=dlnetwork.epochs,
                            dlnetwork=dlnetwork)

        print('==== Network training finished ====')

    else:  # prediction
        predictions = cnnModel.fPredict(X_test=data.X_test,
                          Y_test=Y_test,
                          Y_segMasks_test=data.Y_segMasks_test,
                          sModelPath=savedmodel.savemodel,
                          batch_size=dlnetwork.batchSize,
                          usingClassification=dlnetwork.usingClassification,
                          usingSegmentationMasks=data.usingSegmentationMasks,
                          dlnetwork=dlnetwork)

        if data.usingSegmentationMasks:
            data.handlepredictionssegmentation(predictions)
        else:
            # TODO
        print('==== Network testing finished ====')


if __name__ == "__main__": # for command line call
    # input parsing
    parser = argparse.ArgumentParser(description='''CNN artifact detection''', epilog='''(c) Thomas Kuestner, thomas.kuestner@iss.uni-stuttgart.de''')
    parser.add_argument('-c', '--config', nargs = 1, type = str, help='path to config file', default= 'config/param.yml')
    parser.add_argument('-i','--inPath', nargs = 1, type = str, help='input path to *.mat of stored patches', default= '/med_data/ImageSimilarity/Databases/MRPhysics/CNN/Datatmp/in.mat')
    parser.add_argument('-o','--outPath', nargs = 1, type = str, help='output path to the file used for storage (subfiles _model, _weights, ... are automatically generated)', default= '/med_data/ImageSimilarity/Databases/MRPhysics/CNN/Datatmp/out' )
    parser.add_argument('-m','--model', nargs = 1, type = str, choices =['motion_head_CNN2D', 'motion_abd_CNN2D', 'motion_all_CNN2D', 'motion_CNN3D', 'motion_MNetArt', 'motion_VNetArt', 'multi_DenseResNet', 'multi_InceptionNet'], help='select CNN model', default='motion_2DCNN_head' )
    parser.add_argument('-t','--train', dest='train', action='store_true', help='if set -> training | if not set -> prediction' )
    parser.add_argument('-p','--paraOptim', dest='paraOptim', type = str, choices = ['grid','hyperas','none'], help='parameter optimization via grid search, hyper optimization or no optimization', default = 'none')
    parser.add_argument('-b', '--batchSize', nargs='*', dest='batchSize', type=int, help='batchSize', default=64)
    parser.add_argument('-l', '--learningRates', nargs='*', dest='learningRate', type=int, help='learningRate', default=0.0001)
    parser.add_argument('-e', '--epochs', nargs=1, dest='epochs', type=int, help='epochs', default=300)

    args = parser.parse_args()

    # parse input
    cfg = fParseConfig(args.config[0])

    data = Data(cfg)
    # patch and split into training, val, test set
    data.generateDataset()

    # get network parameters
    dlnetwork = Dlnetwork(cfg)

    print('==== Artifact detection ====')
    fArtDetection(data, dlnetwork, cfg['sMode'])
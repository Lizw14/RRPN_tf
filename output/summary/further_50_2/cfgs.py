# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
import os

"""
yjr spaceNet 
R: 0.747165385117
P: 0.869690533981
mAP: 0.654392926347
F: 0.803785488959
"""

# root path
ROO_PATH = os.path.abspath('/var/lzw/thesis/tf/RRPN_FPN_Tensorflow')

#ROO_PATH = os.path.abspath('../')
print (20*"++--")
print (ROO_PATH)
GPU_GROUP = "4"
USE_MASK = True
ADD_GTBOXES_AS_PROPOSALS = False

SUMMARY_PATH = ROO_PATH + '/output/summary'

TEST_SAVE_PATH = ROO_PATH + '/tools/test_result'
INFERENCE_IMAGE_PATH = ROO_PATH + '/tools/inference_image'
INFERENCE_SAVE_PATH = ROO_PATH + '/tools/inference_results'

NET_NAME = 'resnet_v1_101'
VERSION = 'further_50_2'
CLASS_NUM = 1
BASE_ANCHOR_SIZE_LIST = [32, 64, 128, 256, 512]
LEVEL = ['P2', 'P3', 'P4', 'P5', 'P6']
ANCHOR_STRIDE = [4., 8., 16., 32., 64]
ANCHOR_SCALES = [1.]
ANCHOR_RATIOS = [0.5, 1., 2.0, 3.5, 1/3.5, 5.0, 1/5.0]
ANCHOR_ANGLES = [-90, -75, -60, -45, -30, -15]
SCALE_FACTORS = [10., 10., 5., 5., 2.]
SHORT_SIDE_LEN = 650
DATASET_NAME = 'ship'  # 'ship', 'spacenet', 'pascal', 'coco'
NUM_RECT_PARAMETERS = 5
IOU_USE_GPU = True
NMS_USE_GPU = True
RPN_TRAIN = False

BATCH_SIZE = 1
WEIGHT_DECAY = {'vggnet16': 0.0005, 'resnet_v1_50': 0.0001, 'resnet_v1_101': 0.0001}
EPSILON = 1e-5
MOMENTUM = 0.9
MAX_ITERATION = 250000
LR = 0.0001

# rpn
RPN_NMS_IOU_THRESHOLD = 0.6
MAX_PROPOSAL_NUM = 300
RPN_IOU_POSITIVE_THRESHOLD = 0.6
RPN_IOU_NEGATIVE_THRESHOLD = 0.3
RPN_MINIBATCH_SIZE = 512
RPN_POSITIVE_RATE = 0.5
IS_FILTER_OUTSIDE_BOXES = False
RPN_TOP_K_NMS = 6000
RPN_ANCHOR_ANGLES_THRESHOLD = 15.0
RPN_NMS_ANGLES_THRESHOLD = 15.0
KERNEL_SIZE = 5
FEATURE_PYRAMID_MODE = 0  # {0: 'feature_pyramid'}
SHARED_HEADS=False
USE_HORIZONTAL_NMS = False

# fast rcnn
ROI_SIZE = 14
ROI_POOL_KERNEL_SIZE = 2
USE_DROPOUT = True
KEEP_PROB = 0.5
FAST_RCNN_NMS_IOU_THRESHOLD = 0.35  # 0.6
FAST_RCNN_NMS_MAX_BOXES_PER_CLASS = 100
FINAL_SCORE_THRESHOLD = 0.8  # 0.8
FAST_RCNN_IOU_POSITIVE_THRESHOLD = 0.5
FAST_RCNN_MINIBATCH_SIZE = 128
FAST_RCNN_POSITIVE_RATE = 0.5
FAST_RCNN_TOP_K_NMS = False
FAST_RCNN_BOXES_ANGLES_THRESHOLD = 15.0
FAST_RCNN_NMS_ANGLES_THRESHOLD = 15.0
NEED_AUXILIARY = False

# pretrain weights path
PRETRAINED_CKPT = ROO_PATH + '/data/pretrained_weights/' + NET_NAME + '.ckpt'
# trained weights
TRAINED_CKPT = os.path.join(ROO_PATH, 'output/trained_weights')

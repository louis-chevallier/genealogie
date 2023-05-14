
import ultralytics
ultralytics.checks()

import re, json
import os
import argparse
import torch
from utillc import *
import numpy as np

import utillc
import sys, os, glob
import argparse
from collections import OrderedDict
from collections import defaultdict
import pickle
import cv2
import tqdm
import pandas
import torch
import torchvision
import torch.nn.functional as F
import torch.nn as nn
import torchvision.models as models
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils
import torch.multiprocessing as mp
import albumentations as A
import numpy as np
from glob import glob
import time
import datetime
import imageio
import logging
import glob
#from logging import info
import matplotlib.pyplot as plt 
import lzma
import os, gc
import psutil
from itertools import groupby
import argparse
from torch.utils.tensorboard import SummaryWriter
from itertools import islice
from logging import info
logging.basicConfig(level=logging.INFO,
                    format='%(pathname)s:%(lineno)d: [%(asctime)ss%(msecs)03d]:%(message)s',
                    datefmt='%Hh%Mm%S')

from utillc import *
import datetime
from ultralytics import YOLO

import argparse


import split2

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--size", default=128, type=int)
parser.add_argument("--factor", default=5, type=int)
parser.add_argument("--epoch", default=200, type=int)
parser.add_argument("--train_folder", default="/mnt/hd1/data/manuscript/train_folder")

args = parser.parse_known_args()[0]


ims = glob.glob(os.path.join(args.train_folder, "train", "images", "*.jpg"))

im = cv2.imread(ims[0])
H,W,D = im.shape
EKON(H, W)

# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from scratch
#model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# Use the model

w,h = (args.size*args.factor, args.size*args.factor*2)
w,h = W, H



results = model.train(data='manuscript.yaml',
                      imgsz=(w,h),
                      device=0,
                      optimizer="Adam",
                      project='manuscript',
                      epochs=args.epoch)  # train the model
results = model.val()  # evaluate model performance on the validation set
#results = model("/mnt/hd1/data/manuscript/train_folder/valid/images/n_0093.png")
#r = model.predict("/mnt/hd1/data/manuscript/train_folder/valid/images/n_0093.png")
success = model.export(format='onnx')  # export the model to ONNX format
     

import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
import warnings
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize
# imposta il path dove hai i dati
path = str(r'C:\Users\kevin\project_kevin\ml\Image_Segmentation\Mask_RCNN\samples\coco')
path = path.replace("\\","/")
os.chdir(path)

#pip install pycocotools-windows
import coco






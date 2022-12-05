import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
import warnings

# pip install keras==2.2.5

# Fetching the root directory
# ROOT_DIR = os.path.abspath("../")

warnings.filterwarnings("ignore")
# Importing Mask RCNN 
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize
# Heading to the coco directory
sys.path.append(os.path.join(ROOT_DIR, "samples/coco/"))  
#importing coco.py
import coco
# matplotlib inline
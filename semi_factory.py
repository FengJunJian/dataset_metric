# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

#建立voc数据集格式


"""Factory method for easily getting imdbs by name."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__sets = {}
from semi_pascal_voc import pascal_voc
#from lib.datasets.pascal_voc import pascal_voc
from coco import coco

import numpy as np

# Set up voc_<year>_<split>
__sets['shipdataset']= (lambda image_set='train',devkit_path=None,year='2007': pascal_voc(image_set, year,devkit_path))
__sets['unlabel_dataset']= (lambda image_set='train',devkit_path=None,year='2007': pascal_voc(image_set, year,devkit_path))

def get_imdb(name,image_set='train',dataset_path=None):#image_set=train or test or trainval or val
  """Get an imdb (image database) by name."""
  if name not in __sets:
    raise KeyError('Unknown dataset: {}'.format(name))
  return __sets[name](image_set,dataset_path)


def list_imdbs():
  """List all registered imdbs."""
  return list(__sets.keys())

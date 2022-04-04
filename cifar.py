"""
use cmd line to read data

type in cmd line: 
    "python <path-to-cifar.py> -p <path-to-cifar-dataset>"
to run this script
"""

import numpy as np
from skimage import io
import numpy
import os
import argparse
import re


class CifarReader:
    def __init__(self):
        self.is_initialized = False

    def read_cifar10(self):
        """
        returns: train_egs, train_labels, test_egs, test_labels, labels
            train_egs->list(ndarray): examples of train data
            train_labels->list(str): labels parallel to egs

            test_egs, test_labels: ...

            labels->list(str): all the possible labels in the dataset
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('-p', '--absolute_path', default=u"D:\\work\\作业\\大二\\人工智能综合实验\\cifar", type=str, help="get the absolute path to the root of cifar10 dataset")

        ns, _ = parser.parse_known_args()
        root = ns.absolute_path
        train_root = os.path.join(root, 'train')
        test_root = os.path.join(root, 'test')
        label_root = os.path.join(root, 'labels.txt')

        labels = []
        with open(label_root) as f:
            for line in f.readlines():
                labels.append(re.findall("(.+?)\n", line))

        train_lists = os.listdir(train_root)
        test_lists = os.listdir(test_root)

        train_egs = []
        train_labels = []
        for train_list in train_lists:
            '''
            <number>_<label>.png
            '''
            train_labels.append(re.findall(r"_(.+?).png", train_list))
            img = io.imread(os.path.join(train_root, train_list))
            train_egs.append(img)

        test_egs = []
        test_labels = []
        for test_list in test_lists:
            test_labels.append(re.findall(r"_(.+?).png", test_list))
            img = io.imread(os.path.join(test_root, test_list))
            test_egs.append(img)

        return train_egs, train_labels, test_egs, test_labels, labels

"""
here is what you need to do to call CifarReader
"""
# if __name__ == '__main__':
#     cr = CifarReader()
#     cr.read_cifar10()

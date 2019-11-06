import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import re
import pylab
from pylab import figure, show, legend
from mpl_toolkits.axes_grid1 import host_subplot

# read the log file
fp = open('loss.txt', 'r')
train_iterations = []
train_loss = []

for ln in fp:
    #print(ln)
    if 'step ' in ln and 'loss =' in ln:
        arr = re.findall(r'step \b\d+\b', ln)
        brr = re.findall(r'loss = [0-9]*\.?[0-9]*', ln)
        #print(arr)
        train_iterations.append(int(arr[0][5:len(arr[0])]))
        train_loss.append(float(brr[0][7:len(brr[0])]))
print(train_iterations)
print(train_loss)
fp.close()

#! /usr/bin/env python3
# coding=utf-8

"""
 description:
 author:		kevin.wang
 create date:	2024-04-22
 version:		1.0.0
"""


import os
import numpy as np

import scipy
import scipy.signal

from scipy.signal import find_peaks
import matplotlib.pyplot as plt

from PIL import Image
try:
    # read tiff file with gray
    image = Image.open('Sample-1points.tiff').convert('L')
except Exception as e:
    print(e)
    exit()
image_array = np.array(image)

I = image_array
# get the y position of the spots
tmp = np.sum(I,axis=1)
y0 = np.argmax(tmp)
# crop along the y axis
I = I[y0-96:y0+96,:]

# signal along x
tmp = np.sum(I,axis=0)
tmp[tmp/np.amax(tmp)<0.5] = 0

# find peaks
peak_locations,_ = scipy.signal.find_peaks(tmp,distance=100)
idx = np.argsort(tmp[peak_locations])

peak_0_location = None
peak_1_location = None

if len(idx)>0:
    peak_0_location = peak_locations[idx[-1]]
if len(idx)>1:
    peak_1_location = peak_locations[idx[-2]] # for air-glass-water, the smaller peak corresponds to the glass-water interface
if len(idx)==0:
    raise Exception("did not find any peaks in Laser Reflection Autofocus signal. this is a major problem.")

# choose which surface to use
if peak_1_location is None:
    x1 = peak_0_location
else:
    x1 = peak_1_location

# find centroid
h,w = I.shape
x,y = np.meshgrid(range(w),range(h))
I = I[:,max(0,x1-64):min(w-1,x1+64)]
x = x[:,max(0,x1-64):min(w-1,x1+64)]
y = y[:,max(0,x1-64):min(w-1,x1+64)]
I = I.astype(float)
I = I - np.amin(I)
I[I/np.amax(I)<0.1] = 0
x1 = np.sum(x*I)/np.sum(I)
y1 = np.sum(y*I)/np.sum(I)

x1 = x1 
y1 = y0-96+y1
x_list = []
y_list = []
x_list.append(x1)
y_list.append(y1)
plt.imshow(image_array,cmap="gist_gray")
plt.scatter(x_list,y_list,marker="x",c="green")
plt.show()


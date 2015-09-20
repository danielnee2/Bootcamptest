# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:27:17 2015

@author: niyuli
"""


#image processing

# Our workhorse
import numpy as np

# Our image processing tools
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Seaborn makes plots pretty!
import seaborn as sns


plt.close('all')

# Load the images
im_phase = skimage.io.imread('HG104_phase.tif')
im_fl = skimage.io.imread('HG104_FITC.tif')

#filter median to get rid of bad pixeel
selem = skimage.morphology.square(3)
im_phase_filt = skimage.filters.median(im_phase, selem)
im_fl_filt = skimage.filters.median(im_fl, selem)


# define subregions
r, c = np.indices((200, 300)) + 550

# filter thru otsu
thresh_otsu = skimage.filters.threshold_otsu(im_phase)
im_bw = im_phase_filt < thresh_otsu

# clear border with things touching border
im_bw = skimage.segmentation.clear_border(im_bw, buffer_size=5)

#label the threshholed img
im_labeled, n_labels = skimage.measure.label(im_bw, background=0, return_num=True)

#increment labels by one for furue comaptibility
im_labeled += 1

#Extract porperties
im_props = skimage.measure.regionprops(im_labeled, intensity_image=im_fl_filt)

plt.imshow(im_labeled, cmap=plt.cm.rainbow)
plt.colorbar()

'''
fig, ax = plt.subplots(1, 2)
# show subregion
ax[0].imshow(im_phase, cmap=plt.cm.gray)
ax[1].imshow(im_bw, cmap=plt.cm.gray)'''
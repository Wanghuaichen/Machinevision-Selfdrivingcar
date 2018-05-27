import os
import numpy as np
import cv2

# intencity histogram
def i_histo(img, limit=256, mask=None):
    histo = []

    if mask is not None:
        img = img[mask > 0]

    for i in range(limit):
        histo.append(np.sum(img[img == i]))

    return np.array(histo)

# horizontal histogram
def h_histo(img):
    histo = []
    for q in range(int(img.shape[1]/1)):
        histo.append(np.sum(img[:,q:q+1] > 0))
    return np.array(histo)

# threshold an image based on rgb colors intencity
def threshold(img, lower, upper):
    ret = cv2.inRange(img, lower, upper)
    return ret

# calculate the threshold to show lane lines based on the histogram
def find_lane_threshold(histo, lower, upper):
    ret = cv2.inRange(img, lower, upper)
    return ret

# event_handler for making threshold graphs clickable
_plot_threshold = 0
def threshold_plot_event_handler(event, x, y, flags, param):
    global _plot_threshold
    if event == cv2.EVENT_LBUTTONDOWN:
        _plot_threshold = x

def plot_threshold(w=1):
    return _plot_threshold/w

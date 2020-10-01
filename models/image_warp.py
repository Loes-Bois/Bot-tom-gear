import numpy as np
from urllib.request import urlopen
import cv2
import io
import aiohttp
import discord
import matplotlib.pyplot as plt
import math
import random

def wrap_image(img):
    """
    apply the wrap to image

    """

    # Grab Shape of image
    rows,cols,ch = img.shape

    # Create Points for image warp
    pts1 = np.float32([[1,3],[rows,3],[1,cols],[rows,cols]])
    pts2 = np.float32([[0,0],[rows,0],[0,cols],[rows,cols]])

    # Assemble Transformation Matrix
    M = cv2.getPerspectiveTransform(pts1,pts2)

    # Warp image
    image_wraped = cv2.warpPerspective(img, M, (cols, rows))
    
    # Get Canny(edges) of Image
    edges = cv2.Canny(image_wraped,cols,rows)

    # Fix Color
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Combine Perspective Warp with Canny, preference to Warp
    dst = cv2.addWeighted(edges, 0.2, image_wraped, 0.8, 0.3)

    # Define lookup dict for random transformation to image
    image_transforms = {
        0: vertical_wave,
        1: horizontal_wave,
        2: hor_vert_wave,
        3: concave_wave
    }

    # run random image transformation
    selection = random.randint(1, 1000) % 4
    dst = image_transforms[selection](dst)

    # run random image transformation   
    selection = random.randint(1, 1000) % 4
    dst = image_transforms[selection](dst)
    
    return dst


def vertical_wave(img):
    """
    apply the wrap to images
    """

    rows, cols,ch = img.shape
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(25.0 * math.sin(2 * 3.14 * i / 150))
            offset_y = 0
            if j+offset_x < rows:
                img_output[i,j] = img[i,(j+offset_x)%cols]
            else:
                img_output[i,j] = 0
    return img_output

def horizontal_wave(img):
    """
    apply the wrap to images
    """
    
    rows, cols,ch = img.shape
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = 0
            offset_y = int(16.0 * math.sin(2 * 3.14 * j / 110))
            if i+offset_y < rows:
                img_output[i,j] = img[(i+offset_y)%rows,j]
            else:
                img_output[i,j] = 0
    return img_output


def hor_vert_wave(img):
    """
    apply the wrap to images
    """
    rows, cols,ch = img.shape
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(20.0 * math.sin(2 * 3.14 * i / 100))
            offset_y = int(20.0 * math.cos(2 * 3.14 * j / 120))
            if i+offset_y < rows and j+offset_x < cols:
                img_output[i,j] = img[(i+offset_y)%rows,(j+offset_x)%cols]
            else:
                img_output[i,j] = 0
    return img_output


def concave_wave(img):
    """
    apply the wrap to images
    """

    rows, cols,ch = img.shape
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(128.0 * math.sin(2 * 3.14 * i / (2*cols)))
            offset_y = 0
            if j+offset_x < cols:
                img_output[i,j] = img[i,(j+offset_x)%cols]
            else:
                img_output[i,j] = 0

    return img_output
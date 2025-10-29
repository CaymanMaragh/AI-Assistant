import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

Image(filename='.venv/assets/Checkerboard18*18.png')

cb_img = cv2.imread('.venv/assets/Checkerboard18*18.png', 0)
plt.imshow(cb_img, cmap='gray')
plt.show()



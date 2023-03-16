# https://analityk.edu.pl/python-numpy/
#
# > pip install numpy
# > pip install scikit-image
# > pip install matplotlib

import numpy as np
from skimage import io
import matplotlib.pyplot as plt

pic = np.array(io.imread('fire.jpeg'))
# pic = [0..720][0..1200][230,132,120] (height, width, R,G,B)
plt.imshow(pic)
plt.show()

# flip vertically
plt.imshow(pic[::-1]) # height reversed
plt.show()

# flip horiozpntally
plt.imshow(pic[:,::-1]) # width reversed
plt.show()

# flip both = rotate 180
plt.imshow(pic[::-1,::-1]) # height/width reversed
plt.show()

# resize height
plt.imshow(pic[:,::2])
plt.show()

#
plt.imshow(pic[300:450, 150:600])
plt.show()


# https://analityk.edu.pl/python-numpy/
#
# > pip install numpy
# > pip install scikit-image

import numpy as np
from skimage import io
import matplotlib.pyplot as plt

pic = np.array(io.imread('fire.jpeg'))
plt.imshow(pic)
plt.show()

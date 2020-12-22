import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread 

x =np.arange(0,6,0.1)
y =np.sin(x)

plt.plot(x,y)
plt.show()

img =imread('test.jpg')
plt.imshow(img)

plt.show()
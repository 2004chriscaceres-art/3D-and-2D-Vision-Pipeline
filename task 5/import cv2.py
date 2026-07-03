import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. Create a "dummy" image (a black square with a white circle)
# This removes the need to load any file from your computer!
img = np.zeros((300, 300), dtype="uint8")
cv2.circle(img, (150, 150), 50, 255, -1)

# 2. Now run the exact same pipeline on this dummy image
blurred = cv2.GaussianBlur(img, (7, 7), 0)
edges = cv2.Canny(blurred, 50, 150)

# 3. Show the results
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original (Generated)')
plt.subplot(1, 2, 2), plt.imshow(edges, cmap='gray'), plt.title('Detected Edges')
plt.show()

print("Pipeline success! The vision prototype is working.")
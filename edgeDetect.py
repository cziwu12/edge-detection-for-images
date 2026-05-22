import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

IMG_PATH = input("input image path: ").strip('"\'')
print(IMG_PATH)

img = cv2.imread(IMG_PATH)

blur = cv2.GaussianBlur(img, (5, 5), 0)
canny = cv2.Canny(blur, threshold1=180, threshold2=200)

y_indices, x_indices = np.where(canny == 255)
plt.figure(figsize=(8, 8))

plt.scatter(x_indices, y_indices, color='black', s=0.5)
plt.gca().invert_yaxis()
plt.gca().set_aspect('equal', adjustable='box')

plt.title("Image Converted to Mathematical Graph")
plt.xlabel("X Coordinate (Pixels)")
plt.ylabel("Y Coordinate (Pixels)")
plt.show()

'''
cv2.imshow("Frame View", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
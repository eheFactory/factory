#importing modules

import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt


#load image
img_rgb = cv.imread("h.jpg")

cv.imshow('Original Image',img_rgb)
cv.waitKey(0)



img_g = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scaled Image',img_g)
cv.waitKey(0)



highThresh, threshIm = cv.threshold(img_g, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
lowThresh = 0.5*highThresh

img_edges = cv.Canny(img_g,lowThresh,highThresh)

img_edges = cv.bitwise_not(img_edges)

#numpy_vertical = np.vstack((img_g, img_edges))
numpy_horizontal = np.hstack((img_g, img_edges))

#numpy_vertical_concat = np.concatenate((img_g, img_edges), axis=0)
#numpy_horizontal_concat = np.concatenate((img_g, img_edges), axis=1)
 
#cv.imshow('Numpy Vertical', numpy_vertical)
cv.imshow('Edge Detection', numpy_horizontal)
#cv.imshow('Numpy Vertical Concat', numpy_vertical_concat)
#cv.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)

cv.waitKey(0)
cv.destroyAllWindows()

bw_image_array = np.array(img_edges, dtype=np.int)  
black_indices = np.argwhere(bw_image_array == 0)  
# Changing "size" to a larger value makes this algorithm take longer,  
# but provides more granularity to the portrait  
chosen_black_indices = black_indices[np.random.choice(black_indices.shape[0],  
                                     replace=False,  
                                     size=10000)]

plt.figure(figsize=(6, 8), dpi=100)  
plt.scatter([x[1] for x in chosen_black_indices],  
            [x[0] for x in chosen_black_indices],  
            color='black', s=1)  
plt.gca().invert_yaxis()  
plt.xticks([])  
plt.yticks([])
plt.show()

from scipy.spatial.distance import pdist, squareform  
  
distances = pdist(chosen_black_indices)  
distance_matrix = squareform(distances) 

from tsp_solver.greedy_numpy import solve_tsp  
optimized_path = solve_tsp(distance_matrix)  

optimized_path_points = [chosen_black_indices[x] for x in optimized_path] 


plt.figure(figsize=(8, 10), dpi=60)  
plt.plot([x[1] for x in optimized_path_points],  
         [x[0] for x in optimized_path_points],  
         color='black', lw=1)   
plt.gca().invert_yaxis()  
plt.xticks([])  
plt.yticks([]) 


plt.figure(figsize=(16, 10), dpi=60)  
  
plt.subplot(1, 2, 1)  
plt.imshow(img)  
plt.grid(False)  
plt.xlim(0, 600)  
plt.ylim(0, 800)  
plt.gca().invert_yaxis()  
plt.xticks([])  
plt.yticks([])  
  
plt.subplot(1, 2, 2)  
plt.plot([x[1] for x in optimized_path_points],  
         [x[0] for x in optimized_path_points],  
         color='black', lw=1)  
plt.grid(False)  
plt.xlim(0, 600)  
plt.ylim(0, 800)  
plt.gca().invert_yaxis()  
plt.xticks([])  
plt.yticks([])  


l = len(optimized_path_points)
print(l)
data = ''

for i in range(0,l):
    data = data + '{ x:'+ str(optimized_path_points[i][1]+0.5) + ', y:'+ str(optimized_path_points[i][0]+0.5) + '},'

print(data)
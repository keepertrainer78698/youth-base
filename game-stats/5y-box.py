import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


# Create figure
fig=plt.figure()
fig.set_size_inches(8, 6)
ax=fig.add_subplot(1,1,1)

# Squares
plt.plot([4,4], [0,5.5], color="grey") # outleft
plt.plot([6,6], [0,5.5], color="grey") # left post
plt.plot([8,8], [0,5.5], color="grey") # center left
plt.plot([10,10], [0,5.5], color="grey") # center
plt.plot([12,12], [0,5.5], color="grey") # center rigt
plt.plot([14,14], [0,5.5], color="grey") # right post

plt.plot([0,18.32], [1,1], color="grey") 
plt.plot([0,18.32], [2,2], color="grey") 
plt.plot([0,18.32], [3,3], color="grey") 
plt.plot([0,18.32], [4,4], color="grey") 


plt.text(1, 6, '1 outleft')
plt.text(4.5, 6, '2 lp')
plt.text(6.5, 6, '3 cl')
plt.text(8.5, 6, '4 c')
plt.text(10.5, 6, '5 cr')
plt.text(12.5, 6, '6 rp')
plt.text(15, 6, '7 outright')

plt.text(-1, 0.5, 'A')
plt.text(-1, 1.5, 'B')
plt.text(-1, 2.5, 'C')
plt.text(-1, 3.5, 'D')
plt.text(-1, 4.5, 'E')

# 6-yard Box
plt.plot([0,0],[0,5.5], color="black")
plt.plot([18.32,18.32],[5.5,0], color="black")
plt.plot([0,18.32],[5.5,5.5], color="black")
plt.plot([18.32,0],[0,0], color="black")

# Goal
plt.plot([5.5,12.82],[-2.44,-2.44], color="black")
plt.plot([5.5,5.5],[0,-2.44], color="black")
plt.plot([12.82,12.82],[-2.44,0], color="black")

#Tidy Axes
plt.axis('off')

#Display Pitch
plt.show()
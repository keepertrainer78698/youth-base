import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


# Create figure
fig=plt.figure()
fig.set_size_inches(7, 5)
ax=fig.add_subplot(1,1,1)

# Squares
#plt.plot([5,5], [0,50], color="grey")
plt.plot([10,10], [0,50], color="grey")
#plt.plot([15,15], [0,50], color="grey")
plt.plot([20,20], [0,50], color="grey")
#plt.plot([25,25], [0,50], color="grey")
plt.plot([30,30], [0,50], color="grey")

plt.plot([0,90], [5,5], color="grey")
plt.plot([0,90], [10,10], color="grey")
plt.plot([0,90], [15,15], color="grey")
plt.plot([0,90], [20,20], color="grey")

# Pitch Outline & Centre Line
plt.plot([0,0],[0,50], color="black")
plt.plot([0,90],[50,50], color="black")
plt.plot([90,90],[50,0], color="black")
plt.plot([90,0],[0,0], color="black")

# Penalty Area
plt.plot([65,25],[16.5,16.5], color="black")
plt.plot([25,25],[0,16.5], color="black")
plt.plot([65,65],[16.5,0], color="black")

# 6-yard Box
plt.plot([54,36],[5.5,5.5], color="black")
plt.plot([36,36],[0,5.5], color="black")
plt.plot([54,54],[5.5,0], color="black")

# Penalty Spot
PenSpot = plt.Circle((45,11),0.5,color="black")
ax.add_patch(PenSpot)

# Penalty Arc
Arc = Arc((45,11),height=18.3,width=18.3,angle=90,theta1=310,theta2=50,color="black")
ax.add_patch(Arc)




# #Left Penalty Area
# plt.plot([16.5,16.5],[65,25],color="black")
# plt.plot([0,16.5],[65,65],color="black")
# plt.plot([16.5,0],[25,25],color="black")

# #Right Penalty Area
# plt.plot([130,113.5],[65,65],color="black")
# plt.plot([113.5,113.5],[65,25],color="black")
# plt.plot([113.5,130],[25,25],color="black")

# #Left 6-yard Box
# plt.plot([0,5.5],[54,54],color="black")
# plt.plot([5.5,5.5],[54,36],color="black")
# plt.plot([5.5,0.5],[36,36],color="black")

# #Right 6-yard Box
# plt.plot([130,124.5],[54,54],color="black")
# plt.plot([124.5,124.5],[54,36],color="black")
# plt.plot([124.5,130],[36,36],color="black")

# #Prepare Circles
# centreCircle = plt.Circle((65,45),9.15,color="black",fill=False)
# centreSpot = plt.Circle((65,45),0.8,color="black")
# leftPenSpot = plt.Circle((11,45),0.8,color="black")
# rightPenSpot = plt.Circle((119,45),0.8,color="black")

# #Draw Circles
# ax.add_patch(centreCircle)
# ax.add_patch(centreSpot)
# ax.add_patch(leftPenSpot)
# ax.add_patch(rightPenSpot)

# #Prepare Arcs
# leftArc = Arc((11,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="black")
# rightArc = Arc((119,45),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="black")

# #Draw Arcs
# ax.add_patch(leftArc)
# ax.add_patch(rightArc)

#Tidy Axes
plt.axis('off')

#Display Pitch
plt.show()
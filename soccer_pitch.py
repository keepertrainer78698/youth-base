import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc



def full_pitch():
    # Create figure
    fig=plt.figure()
    fig.set_size_inches(16, 9)
    ax=fig.add_subplot(1,1,1)

    # Pitch Outline & Centre Line
    plt.plot([0,0],[0,100], color="black")
    plt.plot([0,100],[100,100], color="black")
    plt.plot([100,100],[100,0], color="black")
    plt.plot([100,0],[0,0], color="black")

    # Penalty Area 1
    plt.plot([81,19],[16,16], color="black")
    plt.plot([19,19],[0,16], color="black")
    plt.plot([81,81],[16,0], color="black")

    # 6-yard Box
    plt.plot([63,37],[6,6], color="black")
    plt.plot([37,37],[0,6], color="black")
    plt.plot([63,63],[6,0], color="black")

    # Penalty Spot
    PenSpot = plt.Circle((50,10),0.5,color="black")
    ax.add_patch(PenSpot)

    # Penalty Arc
    penalty_arc = Arc((50,10.5),height=18.3,width=18.3,angle=90,theta1=310,theta2=50,color="black")
    ax.add_patch(penalty_arc)

    #Tidy Axes
    plt.axis('off')

    #Display Pitch
    plt.show()


def half_pitch():
    # Create figure
    fig=plt.figure()
    fig.set_size_inches(16, 9)
    ax=fig.add_subplot(1,1,1)

    # Squares
    plt.plot([5,5], [0,50], color="grey") # 1
    plt.plot([10,10], [0,50], color="grey") # 2
    plt.plot([15,15], [0,50], color="grey") # 3
    plt.plot([20,20], [0,50], color="grey") # 4
    plt.plot([25,25], [0,50], color="grey") # 5
    plt.plot([30,30], [0,50], color="grey") # 6
    plt.plot([35,35], [0,50], color="grey") # 7
    plt.plot([40,40], [0,50], color="grey") # 8
    plt.plot([45,45], [0,50], color="grey") # 9
    plt.plot([50,50], [0,50], color="grey") # 10
    plt.plot([55,55], [0,50], color="grey") # 11
    plt.plot([60,60], [0,50], color="grey") # 12
    plt.plot([65,65], [0,50], color="grey") # 13
    plt.plot([70,70], [0,50], color="grey") # 14
    plt.plot([75,75], [0,50], color="grey") # 15
    plt.plot([80,80], [0,50], color="grey") # 16
    plt.plot([85,85], [0,50], color="grey") # 17

    plt.plot([0,90], [5,5], color="grey") # A
    plt.plot([0,90], [10,10], color="grey") # B
    plt.plot([0,90], [15,15], color="grey") # C
    plt.plot([0,90], [20,20], color="grey") # D
    plt.plot([0,90], [25,25], color="grey") # E
    plt.plot([0,90], [30,30], color="grey") # F
    plt.plot([0,90], [35,35], color="grey") # G
    plt.plot([0,90], [40,40], color="grey") # H
    plt.plot([0,90], [45,45], color="grey") # I

    plt.text(2, -2, '1')
    plt.text(7, -2, '2')
    plt.text(12, -2, '3')
    plt.text(17, -2, '4')
    plt.text(22, -2, '5')
    plt.text(27, -2, '6')
    plt.text(32, -2, '7')
    plt.text(37, -2, '8')
    plt.text(42, -2, '9')
    plt.text(46, -2, '10')
    plt.text(51, -2, '11')
    plt.text(56, -2, '12')
    plt.text(61, -2, '13')
    plt.text(66, -2, '14')
    plt.text(71, -2, '15')
    plt.text(76, -2, '16')
    plt.text(81, -2, '17')
    plt.text(86, -2, '18')

    plt.text(-3, 2, 'A')
    plt.text(-3, 7, 'B')
    plt.text(-3, 12, 'C')
    plt.text(-3, 17, 'D')
    plt.text(-3, 22, 'E')
    plt.text(-3, 27, 'F')
    plt.text(-3, 32, 'G')
    plt.text(-3, 37, 'H')
    plt.text(-3, 42, 'I')
    plt.text(-3, 47, 'J')


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
    penalty_arc = Arc((45,10.5),height=18.3,width=18.3,angle=90,theta1=310,theta2=50,color="black")
    ax.add_patch(penalty_arc)

    #Tidy Axes
    plt.axis('off')

    #Display Pitch
    plt.show()


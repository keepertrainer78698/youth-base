import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def full_pitch(background, line, provider):
     # Create figure
    fig=plt.figure()
    fig.set_size_inches(16, 9)
    ax = fig.add_subplot(1,1,1)

     # Set color Scheme
    line_color = line
    fig.set_facecolor(background)

    # Set dimensions Instat
    if provider == "Instat":
        length = 105
        width = 68
        pen_area_x = 16.5
        pen_area_y = 13.85
        pen_area_y2 = 54.15
        six_yard_x = 5.5
        six_yard_y = 24.85
        six_yard_y2 = 43.15
        penalty_spot = [11,34]
    else:
        length = 120
        width = 80
        pen_area_x = 18
        pen_area_y = 18
        pen_area_y2 = 62
        six_yard_x = 6
        six_yard_y = 30
        six_yard_y2 = 50
        penalty_spot = [12,40]


    # Pitch Outline & Centre Line
    plt.plot([0,0],[0,width], color=line_color)
    plt.plot([0,length],[width,width], color=line_color)
    plt.plot([length,length],[width,0], color=line_color)
    plt.plot([length,0],[0,0], color=line_color)
    plt.plot([length / 2, length / 2], [0, width], color=line_color)

    # Left Penalty Area
    plt.plot([0,pen_area_x], [pen_area_y, pen_area_y], color=line_color)
    plt.plot([0,pen_area_x], [pen_area_y2,pen_area_y2], color=line_color)
    plt.plot([pen_area_x,pen_area_x], [pen_area_y,pen_area_y2], color=line_color)

    # Left 6-yard Box
    plt.plot([0,six_yard_x], [six_yard_y, six_yard_y], color=line_color)
    plt.plot([0,six_yard_x], [six_yard_y2,six_yard_y2], color=line_color)
    plt.plot([six_yard_x,six_yard_x], [six_yard_y,six_yard_y2], color=line_color)

    # Left Penalty Spot
    PenSpot = plt.Circle(penalty_spot,0.5, color=line_color)
    ax.add_patch(PenSpot)

    # Left Penalty Arc
    penalty_arc = Arc(penalty_spot,height=18.3,width=18.3,angle=360,theta1=307,theta2=53, color=line_color)
    ax.add_patch(penalty_arc)

     # Right Penalty Area
    plt.plot([length,length - pen_area_x], [width - pen_area_y, width - pen_area_y], color=line_color)
    plt.plot([length, length - pen_area_x], [width - pen_area_y2, width - pen_area_y2], color=line_color)
    plt.plot([length - pen_area_x, length - pen_area_x], [width - pen_area_y, width - pen_area_y2], color=line_color)

    # Right 6-yard Box
    plt.plot([length, length - six_yard_x], [width - six_yard_y, width - six_yard_y], color=line_color)
    plt.plot([length, length - six_yard_x], [width - six_yard_y2, width - six_yard_y2], color=line_color)
    plt.plot([length - six_yard_x, length - six_yard_x], [width - six_yard_y, width - six_yard_y2], color=line_color)

    # Right Penalty Spot
    PenSpot = plt.Circle((length-penalty_spot[0], penalty_spot[1]),0.5, color=line_color)
    ax.add_patch(PenSpot)

    # Right Penalty Arc
    penalty_arc = Arc((length-penalty_spot[0], penalty_spot[1]),height=18.3,width=18.3,angle=180,theta1=307,theta2=53, color=line_color)
    ax.add_patch(penalty_arc)

    #Prepare Circles
    centreCircle = plt.Circle((length/2, width/2),9.15,color=line_color, fill=False)
    centreSpot = plt.Circle((length/2, width/2),0.8,color=line_color)
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
 
    #Tidy Axes
    plt.axis('off')


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


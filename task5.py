import random
from random import choice
import math
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import uniform

r = 100
pathx = [0]
pathy = [0]
steps = 200000
circle_theta = np.linspace(0, 2*np.pi)
x1 = r*np.cos(circle_theta)
y1 = r*np.sin(circle_theta)
for i in range(steps):
    check = False
    theta = uniform.rvs(size=1, loc = 0, scale=360)
    theta = (theta[0]*math.pi)/180
    r2 = uniform.rvs(size=1, loc = 0, scale=1)
    r2 = r2[0]
    h = pathx[-1]
    k = pathy[-1]
    x2 = r2*math.cos(theta)+h
    y2 = r2*math.sin(theta)+k
    while (check == False):
        if (x2**2 + y2**2) > r**2:
            theta = math.atan(y2/x2)
            x3 = r*math.cos(theta)
            y3 = r*math.sin(theta)
            pathx.append(x3)
            pathy.append(y3)
            if (((x2 > 0) & (y2 > 0)) | ((x2 > 0) & (y2 < 0))): #When point is outside but in first and fourth quadrant 
                x2 = x3 - (x2 - x3)
                y2 = y3
            else:
                x2 = x3 + (x3 - x2)
                y2 = y3
        else:
            pathx.append(x2)
            pathy.append(y2)
            check = True
fig, ax = plt.subplots(1)
ax.plot(x1, y1)
circle = plt.Circle((0, 0), 1)
plt.plot(pathx,pathy)
plt.legend(["Circle", "Plot"])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

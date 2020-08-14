import random
from random import choice
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
from statistics import mean


class Node:
    def __init__(self, x_initial: float, y_inital: float):
        self.pathx, self.pathy = [x_initial], [y_inital]

    def random_theta(self):
        '''
        returns random orientation
        '''

        return (uniform.rvs(size=1, loc=0, scale=360)[0]*math.pi)/180

    def random_step(self):
        '''
        returns random step size
        '''
        return uniform.rvs(size=1, loc=0, scale=1)[0]

    def change_path(self):
        '''
        Move the node along a random path
        '''
        h = self.pathx[-1]
        k = self.pathy[-1]
        theta, r2 = self.random_theta(), self.random_step()
        x2 = r2*math.cos(theta)+h
        y2 = r2*math.sin(theta)+k
        check = False
        while check == False:
            if (x2**2 + y2**2) > 100**2:
                theta = math.atan(y2/x2)
                x3 = r2*math.cos(theta)
                y3 = r2*math.sin(theta)
                self.pathx.append(x3)
                self.pathy.append(y3)
                # When point is outside but in first and fourth quadrant
                if (((x2 > 0) & (y2 > 0)) | ((x2 > 0) & (y2 < 0))):
                    x2 = x3 - (x2 - x3)
                    y2 = y3
                else:
                    x2 = x3 + (x3 - x2)
                    y2 = y3
            else:
                self.pathx.append(x2)
                self.pathy.append(y2)
                check = True

    def get_pathx(self):
        return self.pathx

    def get_pathy(self):
        return self.pathy


class Steps:
    def __init__(self):
        self.steps = 0

    def check_distance(self, node: Node, node1: Node):
        '''
        checks is the distance is less than one or not
        '''

        pos_x, pos_y = node.get_pathx()[-1], node.get_pathy()[-1]
        pos_x1, pos_y1 = node1.get_pathx()[-1], node1.get_pathy()[-1]

        distance = math.sqrt((pos_x-pos_x1)**2 + (pos_y-pos_y1)**2)
        return distance <= 1

    def calculate_steps(self, node: Node, node1: Node):
        '''
        calculate no. of steps until the distance reduces to less or equal to 1 or when the step
        exceed 10,000
        '''

        while True:

            if self.check_distance(node, node1):
                return self.steps
            else:
                node.change_path()
                node1.change_path()
                if self.steps < 10000:
                    self.steps += 1
                else:
                    return 10000


def average_steps(simulations_no):
    """return a list of number of steps after every simulation"""

    final = []
    running = simulations_no
    while simulations_no:
        print("running simulation number:", running-simulations_no+1)
        step1 = Steps()
        node = Node(0, 0)
        node1 = Node(2, 2)
        #print("Calculating steps", step1.calculate_steps(node, node1))
        final.append(step1.calculate_steps(node, node1))
        simulations_no -= 1
    return final


# making the histogram

no_simulations = int(input("Number of simulation?"))

data = average_steps(no_simulations)

plt.hist(data, color='r', edgecolor='k', alpha=0.65)
plt.axvline(mean(data), color='k', linestyle='dashed', linewidth=1)

min_ylim, max_ylim = plt.ylim()
plt.text(mean(data)*1.1, max_ylim*0.9, 'Average: {:.2f}'.format(mean(data)))

plt.xlabel("steps taken")
plt.ylabel("frequency")
plt.show()

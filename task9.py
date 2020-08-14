import random
from random import choice
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform


def draw_circle():
    x1 = 100*np.cos(np.linspace(0, 2*np.pi))
    y1 = 100*np.sin(np.linspace(0, 2*np.pi))
    fig, ax = plt.subplots()
    ax.plot(x1, y1)


class Node:
    def __init__(self, position: tuple, corona: bool, distance: bool):
        self.pathx, self.pathy = [position[0]], [position[1]]
        self.corona = corona
        if distance:
            self.step = 0.5
        else:
            self.step = 2

    def random_theta(self):
        return (uniform.rvs(size=1, loc=0, scale=360)[0]*math.pi)/180

    def change_path(self):
        h = self.pathx[-1]
        k = self.pathy[-1]
        theta = self.random_theta()
        x2 = self.step*math.cos(theta)+h
        y2 = self.step*math.sin(theta)+k
        check = False
        while check == False:
            if (x2**2 + y2**2) > 100**2:
                theta = math.atan(y2/x2)
                x3 = self.step*math.cos(theta)
                y3 = self.step*math.sin(theta)
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

    def plot(self):
        if self.corona:
            plt.plot(self.pathx, self.pathy, 'r')
        else:
            colors = ['y', 'g', 'b', 'c', 'm', 'k']
            clr = random.choice(colors)
            plt.plot(self.pathx, self.pathy, clr)


class Steps:
    def __init__(self):
        self.steps = 0

    def check_distance(self, node: Node, node1: Node):
        pos_x, pos_y = node.get_pathx()[-1], node.get_pathy()[-1]
        pos_x1, pos_y1 = node1.get_pathx()[-1], node1.get_pathy()[-1]

        distance = math.sqrt((pos_x-pos_x1)**2 + (pos_y-pos_y1)**2)
        if (node.corona or node1.corona) and distance <= 6:
            print("case confirmed")
            node.corona = node1.corona = True
            return True
        return False


'''                 P   L   O   T   T   I   N   G                   '''


stps = int(input("Number of steps: "))
# with distance
print("With practicing social distance")
draw_circle()

corona, node1, node2, node3 = Node((25, 25), True, True), Node(
    (-25, -25), False, True), Node((-25, 25), False, True), Node((25, -25), False, True)

steps = Steps()
for i in range(stps):
    corona.change_path()
    node1.change_path()
    node2.change_path()
    node3.change_path()
    steps.check_distance(corona, node1)
    steps.check_distance(corona, node2)
    steps.check_distance(corona, node3)

corona.plot()
node1.plot()
node2.plot()
node3.plot()
plt.legend(["Circle", "corona", "node1", "node2", "node3"],)
plt.title("Social Distancing")
plt.show()


# without distance
print("Without practicing social distance")
draw_circle()
corona, node1, node2, node3 = Node((25, 25), True, False), Node(
    (-25, -25), False, False), Node((-25, 25), False, False), Node((25, -25), False, False)


steps = Steps()
for i in range(stps):
    corona.change_path()
    node1.change_path()
    node2.change_path()
    node3.change_path()
    steps.check_distance(corona, node1)
    steps.check_distance(corona, node2)
    steps.check_distance(corona, node3)

corona.plot()
node1.plot()
node2.plot()
node3.plot()
plt.legend(["Circle", "corona", "node1", "node2", "node3"])
plt.title("Social Distancing")
plt.show()

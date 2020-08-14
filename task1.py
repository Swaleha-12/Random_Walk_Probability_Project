#Task1:
import random 
import numpy as np 
import matplotlib.pyplot as plt
from random import choices
import statistics

def path_finder(steps, prob, path):
    pos = 0
    for i in range(steps):
        choice = random.choices([1,-1], prob)  #Selects 1 & -1 with the corresponding probabilties specified in prob list. 
        pos = path[-1] + choice[0]
        path.append(pos)
    return path

def freqn(n,bins,patches):
    nmax = max(n)
    for i in range(len(n)):
        if (n[i] == nmax):
            return patches.pop(i)

p = float(input("Enter the probability to move right (p): "))
steps = int(input("Enter the number of steps taken: "))
start_pos = int(input("Enter the starting position: "))
prob = [p, round(float(1.0-p), 1)] #p = prob to move right and 1-p = prob to move left
print(prob)
path = [start_pos]
path_histo = []
for i in range(1000):
    path2 = path_finder(steps, prob, path)
    path_histo.append(abs(path[-1]-start_pos))
    path = [start_pos]
print("Starting position = ", start_pos)
path_histo.sort()
print("path: ", path_histo)
n, bins, patches = plt.hist(x=path_histo, bins=path_histo, color='#0504aa', alpha=0.7, histtype='bar', ec='black')
print("n: ", n)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Task 1')
maxfreq = freqn(n,bins,patches)
print("Expected distance from starting point: ", maxfreq)
plt.show()

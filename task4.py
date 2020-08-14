#Task 4:
import random 
import numpy as np 
import matplotlib.pyplot as plt
from random import choices
from scipy.stats import uniform
import statistics

def path_finder(steps, prob, path):
    pos = 0
    for i in range(steps):
        choice = uniform.rvs(size=1, loc = 0, scale=1)  #Selects continuous value uniformly distributed between 0 & 1. 
        choice = choice[0]
        pos = path[-1] + choice
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
n, bins, patches = plt.hist(x=path_histo, bins='auto', color='#0504aa', alpha=0.7, histtype='bar', ec='black')
print("n: ", n)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Task 4')
maxfreq = freqn(n,bins,patches)
print("Bin: ", bins)
print("Patches: ", patches)
print("Expected distance from starting point: ", maxfreq)
plt.show()

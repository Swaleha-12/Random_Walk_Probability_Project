#TASK2:
import random 
import numpy as np 
import matplotlib.pyplot as plt
import time
import math
from random import choices
from random import choices
import statistics

def freqn(n,bins,patches):
    nmax = max(n)
    for i in range(len(n)):
        if (n[i] == nmax):
            return patches.pop(i)

p1 = float(input("Enter the right probability of person 1: "))
p2 = float(input("Enter the right probability of person 2: "))
s1 = int(input("Enter the starting position of person 1: "))
s2 = int(input("Enter the starting position of person 2: "))
prob1 = [p1, round(float(1-p1),1)]
prob2 = [p2, round(float(1-p2),1)]
x = abs(s1-s2)
path1 = [s1]
path2 = [s2]
check = False
pos1 = 0
pos2 = 0  
time = 0    #Assumption = This time is equivalent to real time so if time = 5 then it is equal to 5 seconds.
time_histo = []
for i in range(1000):
    while (check == False):
        choice1 = choices([1,-1], prob1)  #Selects 1 & -1 with the corresponding probabilties specified in prob1 list. 
        choice2 = choices([1,-1], prob2)  #Selects 1 & -1 with the corresponding probabilties specified in prob2 list.
        pos1 = path1[-1] + choice1[0]
        pos2 = path2[-1] + choice2[0]
        path1.append(pos1)
        path2.append(pos2)
        time+=1
        if path1[-1] == path2[-1]:
            check = True
        if time == 100: #Will wait for 100seconds if path don't meet it will end
            break
    time_histo.append(time)
    path1 = [s1]
    path2 = [s2]
    pos1 = 0
    pos2 = 0
    check = False
    time = 0    #Assumption = This time is equivalent to real time so if time = 5 then it is equal to 5 seconds.
time_histo.sort()
print("Time histo: ", time_histo)
n, bins, patches = plt.hist(x=time_histo, bins=time_histo, color='#0504aa', alpha=0.7, histtype='bar', ec='black')
print("Starting position of p1 = ", s1)
print("Starting position of p2 = ", s2)
plt.xlabel('time')
plt.ylabel('Frequency')
plt.title('Task 2')
maxfreq = freqn(n,bins,patches)
print("Expected time taken: ", maxfreq)
plt.show()

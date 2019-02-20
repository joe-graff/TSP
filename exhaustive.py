import math
import itertools
import random
import time
import helperFunctions

#Calculates distance between two points
def checkDist(a,b):
    return math.sqrt(math.pow(a,2) + math.pow(b,2))

#Implements exhaustive solution to Traveling Salesperson
def run(x,y,numPoints):
    numPoints = numPoints
    xPoints = x
    yPoints = y
    base = ""
    distances = []
    for i in range(0,len(xPoints)):
        base += str(i)
    perm = list(itertools.permutations(base,numPoints)) #create all possible permutations of the points
    firsts = []
    #always begin at the given starting point
    for i in perm:
        if(i[0] == str(0)):
            firsts.append(i)
    #calculate the total distance traveled for each permutation
    for x in firsts:
        dist = 0
        for i in range(0,numPoints-1):
            tempx = xPoints[int(x[i])]
            tempy = yPoints[int(x[i])]
            dist += checkDist(abs(tempx-xPoints[int(x[i+1])]),abs(tempy-yPoints[int(x[i+1])]))
        dist += checkDist(abs(xPoints[0]-xPoints[int(x[numPoints-1])]),abs(yPoints[0]-yPoints[int(x[numPoints-1])]))
        distances.append(dist)
    smallest = 0;
    #find the shortest distance
    for x in range(0,len(distances)):
        if(distances[x] < distances[smallest]):
            smallest = x
    print(round(distances[smallest],2))
    for x in range(0,numPoints):
        helperFunctions.printPoint(xPoints[int(firsts[smallest][x])],yPoints[int(firsts[smallest][x])])
    helperFunctions.printPoint(xPoints[int(firsts[smallest][0])],yPoints[int(firsts[smallest][0])])

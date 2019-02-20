import math
import itertools
import random
import time
import helperFunctions

#Returns the total number of visited points
def totalVisited(x):
    total = 0;
    for i in range(len(x)):
        total += x[i]
    return total

#Implements the nearest Neighbor solution to Traveling Salesperson
def run(x,y,numPoints):
    numPoints = numPoints
    xPoints = x
    yPoints = y
    totalDistance = 0.0;
    visited = []
    order = []
    for i in range(0,numPoints):
        if(i == 0):
            visited.append(1); #mark the first point as visited (starting point)
        else:
            visited.append(0);
    order.append(0)
    currPoint = 0
    nextPoint = 0
    #Decide the closest neighbor and move to that point then decide on the next
    while(totalVisited(visited) != numPoints):
        dist = float('inf')
        for i in range(0,numPoints):
            distance = helperFunctions.checkDist(abs(xPoints[i]-xPoints[currPoint]),abs(yPoints[i]-yPoints[currPoint]))
            if(distance < dist and visited[i] == 0):
                dist = distance
                nextPoint = i
        visited[nextPoint] = 1
        totalDistance += dist
        currPoint = nextPoint
        order.append(nextPoint)
    totalDistance += helperFunctions.checkDist(abs(xPoints[0] - xPoints[order[len(order)-1]]),abs(yPoints[0] - yPoints[order[len(order)-1]])) #calculate the distance to return to begining
    order.append(0)
    print(round(totalDistance,2))
    for i in range(0,numPoints+1):
        helperFunctions.printPoint(xPoints[order[i]],yPoints[order[i]])

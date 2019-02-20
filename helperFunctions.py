import math
#Print the point given by the x and y coordinate
def printPoint(x,y):
    print("(" + str(x) + "," + str(y) + ")")

#Calculates distance between two points
def checkDist(a,b):
    return math.sqrt(math.pow(a,2) + math.pow(b,2))

import nearestNeighbor
import exhaustive

input = open("testfile","r")
lines = input.read().splitlines()
numPoints = int(lines[0])
other = lines[1:]
count = 0
x = []
y = []
for i in other:
    temp = i.split()
    x.append(int(temp[0]))
    y.append(int(temp[1]))
    count += 1
print("Exhaustive Solution:")
exhaustive.run(x,y,numPoints)
print("Nearest Neighbor Solution:")
nearestNeighbor.run(x,y,numPoints)

#commented out testing because of varrying input

# #trial 1
# trialx = []
# trialy = []
# numPoints = 8
# for t in range(0,numPoints):
#     x = random.randint(0,100)
#     y = random.randint(0,100)
#     trialx.append(x)
#     trialy.append(y)
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime1_1 = time.time() - startTime
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime1_2 = time.time() - startTime
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime1_3 = time.time() - startTime
#
# avg = ((runTime1_1+runTime1_2+runTime1_3)/3)
# print("Exhaustive " + str(numPoints) + " " + str(avg))
#
# #Round 2
# trialx = []
# trialy = []
# numPoints = 9
# for t in range(0,numPoints):
#     x = random.randint(0,100)
#     y = random.randint(0,100)
#     trialx.append(x)
#     trialy.append(y)
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime2_1 = time.time() - startTime
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime2_2 = time.time() - startTime
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime2_3 = time.time() - startTime
#
# avg = ((runTime2_1+runTime2_2+runTime2_3)/3)
# print("Exhaustive " + str(numPoints) + " " + str(avg))
#
# #Round 3
# trialx = []
# trialy = []
# numPoints = 10
# for t in range(0,numPoints):
#     x = random.randint(0,100)
#     y = random.randint(0,100)
#     trialx.append(x)
#     trialy.append(y)
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime3_1 = time.time() - startTime
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime3_2 = time.time() - startTime
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime3_3 = time.time() - startTime
#
# avg = ((runTime3_1+runTime3_2+runTime3_3)/3)
# print("Exhaustive " + str(numPoints) + " " + str(avg))
#
#
# #Round 4
# trialx = []
# trialy = []
# numPoints = 11
# for t in range(0,numPoints):
#     x = random.randint(0,100)
#     y = random.randint(0,100)
#     trialx.append(x)
#     trialy.append(y)
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime4_1 = time.time() - startTime
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime4_2 = time.time() - startTime
#
# startTime = time.time()
# exhaustive(trialx,trialy)
# runTime4_3 = time.time() - startTime
#
# avg = ((runTime4_1+runTime4_2+runTime4_3)/3)
# print("Exhaustive " + str(numPoints) + " " + str(avg))

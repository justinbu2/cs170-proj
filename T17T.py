import sys
from itertools import permutations
import os
import glob

def main(argv):
  if len(argv) != 1:
    print "Usage: python validator.py [path_to_input_file]"
    return
  path = argv[0]

  for filename in glob.glob(os.path.join(path, '*.in')):
    T17T(filename)

def T17T(argv):
  x = processFile(argv)
  if len(x) != 3:
    print x
    return
  #print (x)
  cityNum = x[0] #number of cities (50)
  adjMatrix = x[1] #the adjacency matrix adjMatrix[i][j] = 0-100
  colorArray = x[2] #color of city #, colorArray[50] = B

  #print output(T17Tgreedy(cityNum, adjMatrix, colorArray)[1])
  routes = []
  routes.append(T17Tgreedy(cityNum, adjMatrix, colorArray))
  minRoute = [sys.maxint,0]
  for i in range(0, len(routes)):
    currRoute = routes[i]
    if minRoute[0] > currRoute[0]:
      minRoute = currRoute

  print output(minRoute[1])

def T17Tgreedy(cityNum, adjMatrix, colorArray):#Runs greedysearch on all citys as a start and takes min
  #cityNum = number of cities (50)
  #adjMatrix = the adjacency matrix adjMatrix[i][j] = 0-100
  #colorArray = color of city #, colorArray[50] = B
  minRoute = [sys.maxint,0]
  for i in range(0, cityNum):
    currRoute = greedySearch(i, adjMatrix, colorArray)
    #print currRoute
    if minRoute[0] > currRoute[0]:
      minRoute = currRoute
  #print minRoute[0]
  return minRoute

def greedySearch(start, adjMatrix, colorArray): #picks next smallest valid city
  colorCnt = 1
  currColor = colorArray[start]
  currCity = start
  ucityList = list(range(0,len(adjMatrix)))
  pathcost = 0
  routeTrack = []
  routeTrack.append(currCity)

  for i in range(0,len(adjMatrix)-1):
    minNext = smallestNext(currCity, 101, currColor, colorCnt, ucityList, adjMatrix, colorArray)
    currCity = minNext[0][0]
    pathcost += minNext[0][1]
    routeTrack.append(currCity)
    if currColor == minNext[1]:
      colorCnt += 1
    else:
      colorCnt = 1
      currColor = minNext[1]
    #print ("color count is " + str(colorCnt))
    #ucityList[currCity] = -1
  #print pathcost
  return [pathcost,routeTrack]

def smallestNext(currCity, minCost, currColor, count, ucityList, adjMatrix, colorArray):
  minNext = [[currCity,minCost], currColor, 0]
  #loop through ucityList
  #find min valid next path
  colorCnt = count
  for i in range(0, len(ucityList)):
    if ucityList[i] == currCity:
      ucityList[i] = -1
      continue
    if ucityList[i] < 0:
      continue
    elif colorArray[ucityList[i]] == currColor and colorCnt >= 3:
      continue
    else:
      if minNext[0][1] > adjMatrix[currCity][ucityList[i]]:
        minNext[0][1] = adjMatrix[currCity][ucityList[i]]
        minNext[0][0] = ucityList[i]
        minNext[1] = colorArray[ucityList[i]]
  return minNext

def output(array):
  rbout = ""
  for i in range(0, len(array)):
    rbout = rbout + " " + str(array[i]+1)
  #print rb
  return rbout.strip()

def processFile(s):
  fin = open(s, "r")
  line = fin.readline().split()
  if len(line) != 1 or not line[0].isdigit():
    return ("Line 1 must contain a single integer.")
  N = int(line[0])
  if N < 4 or N > 50 or N % 2 != 0:
    return ("N must be an even integer between 4 and 50, inclusive.")

  cityNum = N

  d = [[0 for j in range(N)] for i in range(N)]

  for i in xrange(N):
    line = fin.readline().split()
    if len(line) != N:
      return "Line " + `i+2` + " must contain N integers."
    for j in xrange(N):
      if not line[j].isdigit():
        return "Line " + `i+2` + " must contain N integers."
      d[i][j] = int(line[j])
      a = int(line[j])
      if d[i][j] < 0 or d[i][j] > 100:
        return "All edge weights must be between 0 and 100, inclusive."

  for i in xrange(N):
    if d[i][i] != 0:
      return "The distance from a node to itself must be 0."
    for j in xrange(N):
      if d[i][j] != d[j][i]:
        return "The distance matrix must be symmetric."

  adjMatrix = d

  line = fin.readline().strip()

  if len(line) != N:
    return "Line " + `N+2` + " must be a string of length N."

  r = 0
  b = 0

  x = []
  for j in xrange(N):
    c = line[j]
    if c != 'R' and c != 'B':
      return "Each character of the string must be either R or B."
    if c == 'R': r += 1
    if c == 'B': b += 1
    x.append(c)

  if r != b:
    return "The number of red and blue cities must be equal."

  colorArray = x

  line = fin.readline()
  if len(line) != 0:
    return "The file must have exactly N+2 lines."

  output = []
  output.append(cityNum)
  output.append(adjMatrix)
  output.append(colorArray)

  return output

if __name__ == '__main__':
    main(sys.argv[1:])
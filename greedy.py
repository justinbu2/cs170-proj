import sys
from itertools import permutations
import os
import glob

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
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
    currRoute = greedySearch(i, adjMatrix, colorArray, 1)
    #print currRoute
    if minRoute[0] > currRoute[0]:
      minRoute = currRoute

  return minRoute

def T17Tgreedy2(cityNum, adjMatrix, colorArray):#Runs greedysearch on all citys as a start and takes min
  #cityNum = number of cities (50)
  #adjMatrix = the adjacency matrix adjMatrix[i][j] = 0-100
  #colorArray = color of city #, colorArray[50] = B
  minRoute = [sys.maxint,0]
  for i in range(0, cityNum):
    currRoute = greedySearch(i, adjMatrix, colorArray, 2)
    #print currRoute
    if minRoute[0] > currRoute[0]:
      minRoute = currRoute

  return minRoute

def greedySearch(start, adjMatrix, colorArray, number): #picks next smallest valid city
  colorCnt = 1
  rCount = 0
  bCount = 0
  currColor = colorArray[start]
  currCity = start
  startColor = colorArray[start]
  #print startColor
  ucityList = list(range(0,len(adjMatrix)))
  pathcost = 0
  routeTrack = []
  routeTrack.append(currCity)
  if startColor == 'R':
    rCount += 1
  else:
    bCount += 1


  for i in range(0,len(adjMatrix)-1):
    if number == 1:
      minNext = smallestNext(currCity, currColor, colorCnt, rCount, bCount, ucityList, adjMatrix, colorArray, routeTrack)
    else:
      minNext = smallestNext2(currCity, currColor, colorCnt, rCount, bCount, ucityList, adjMatrix, colorArray, routeTrack)
    currCity = minNext[0][0]
    pathcost += minNext[0][1]
    routeTrack.append(currCity)
    if minNext[1] == 'R':
      rCount += 1
    else:
      bCount += 1

    if currColor == minNext[1]:
      colorCnt += 1
    else:
      colorCnt = 1
      currColor = minNext[1]

    #print minNext
    #print (len(adjMatrix)/2)-rCount, (len(adjMatrix)/2)-bCount
    #print routeTrack
    #print ("color count is " + str(colorCnt))
    #ucityList[currCity] = -1
  #print pathcost
  return [pathcost,routeTrack]

def smallestNext(currCity, currColor, count, rCount, bCount, ucityList, adjMatrix, colorArray, routeTrack):
  minNext = [[currCity,sys.maxint], currColor, 0]
  colorCnt = count
  for i in range(0, len(ucityList)):
    if ucityList[i] == currCity:
      ucityList[i] = -1
      continue
    if ucityList[i] < 0:
      continue
    if colorArray[ucityList[i]] == currColor and colorCnt >= 3:
      continue
    if colorArray[ucityList[i]] == 'R' and ((len(adjMatrix)/2) - rCount)*3 < ((len(adjMatrix)/2) - bCount) and ((len(adjMatrix)/2) - rCount) != 0:
      continue
    if colorArray[ucityList[i]] == 'B' and ((len(adjMatrix)/2) - bCount)*3 < ((len(adjMatrix)/2) - rCount) and ((len(adjMatrix)/2) - bCount) != 0:
      continue
    if minNext[0][1] > adjMatrix[currCity][ucityList[i]]:
        minNext[0][1] = adjMatrix[currCity][ucityList[i]]
        minNext[0][0] = ucityList[i]
        minNext[1] = colorArray[ucityList[i]]
        break
  #loop through ucityList
  #find min valid next path
  
  for i in range(0, len(ucityList)-1):
    if ucityList[i] == currCity:
      ucityList[i] = -1
      continue
    if ucityList[i] < 0:
      continue
    if colorArray[ucityList[i]] == currColor and colorCnt >= 3:
      continue
    if colorArray[ucityList[i]] == 'R' and ((len(adjMatrix)/2) - rCount)*3 < ((len(adjMatrix)/2) - bCount) and ((len(adjMatrix)/2) - rCount) != 0:
      continue
    if colorArray[ucityList[i]] == 'B' and ((len(adjMatrix)/2) - bCount)*3 < ((len(adjMatrix)/2) - rCount) and ((len(adjMatrix)/2) - bCount) != 0:
      continue
    if minNext[0][1] > adjMatrix[currCity][ucityList[i]]:
        minNext[0][1] = adjMatrix[currCity][ucityList[i]]
        minNext[0][0] = ucityList[i]
        minNext[1] = colorArray[ucityList[i]]
  return minNext

def smallestNext2(currCity, currColor, count, rCount, bCount, ucityList, adjMatrix, colorArray, routeTrack):
  minNext = [[currCity,sys.maxint], currColor, 0]
  colorCnt = count
  for i in range(0, len(ucityList)):
    if ucityList[i] == currCity:
      ucityList[i] = -1
      continue
    if ucityList[i] < 0:
      continue
    if colorArray[ucityList[i]] == currColor and colorCnt >= 3:
      continue
    if colorArray[ucityList[i]] == 'R' and ((len(adjMatrix)/2) - rCount)*3 < ((len(adjMatrix)/2) - bCount) and ((len(adjMatrix)/2) - rCount) != 0:
      continue
    if colorArray[ucityList[i]] == 'B' and ((len(adjMatrix)/2) - bCount)*3 < ((len(adjMatrix)/2) - rCount) and ((len(adjMatrix)/2) - bCount) != 0:
      continue
    if minNext[0][1] >= adjMatrix[currCity][ucityList[i]]:
        minNext[0][1] = adjMatrix[currCity][ucityList[i]]
        minNext[0][0] = ucityList[i]
        minNext[1] = colorArray[ucityList[i]]
        break
  #loop through ucityList
  #find min valid next path
  
  for i in range(0, len(ucityList)-1):
    if ucityList[i] == currCity:
      ucityList[i] = -1
      continue
    if ucityList[i] < 0:
      continue
    if colorArray[ucityList[i]] == currColor and colorCnt >= 3:
      continue
    if colorArray[ucityList[i]] == 'R' and ((len(adjMatrix)/2) - rCount)*3 < ((len(adjMatrix)/2) - bCount) and ((len(adjMatrix)/2) - rCount) != 0:
      continue
    if colorArray[ucityList[i]] == 'B' and ((len(adjMatrix)/2) - bCount)*3 < ((len(adjMatrix)/2) - rCount) and ((len(adjMatrix)/2) - bCount) != 0:
      continue
    if minNext[0][1] >= adjMatrix[currCity][ucityList[i]]:
        minNext[0][1] = adjMatrix[currCity][ucityList[i]]
        minNext[0][0] = ucityList[i]
        minNext[1] = colorArray[ucityList[i]]
  return minNext
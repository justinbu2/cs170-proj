import copy

def enumerateAllPossibilities(adjMatrix, colorArray, threshold):
    possibilities = set() # set of [pathLength, path]
    cityNum = len(adjMatrix)
    ucityList = [i for i in range(0, len(colorArray))]
    for s in range(0, cityNum):
        sColor = colorArray[s]
        if sColor == 'R':
            possibilities.add(visit(adjMatrix, s, sColor, 1, 0, 1, threshold, ucityList, [s], 0)) # within DFS, if sum of path length exceeds threshold, return None
        elif sColor == 'B':
            possibilities.add(visit(adjMatrix, s, sColor, 0, 1, 1, threshold, ucityList, [s], 0)) # within DFS, if sum of path length exceeds threshold, return None
        else:
            raise Exception("invalid color for starting node")
        
    return min(possibilites, cmp=lambda x,y: cmp(x[0], y[0]))

def visit(adjMatrix, x, xColor, rCount, bCount, currColorCnt, threshold, ucityList, pathSoFar, pathLength):
    "Returns a tuple of (weight, [totalPath])"
    #rCount is the number of Reds total so far
    #bCount is the number of Blues total so far
    #pathLength is the sum of the weights of edges so far
    if sum >= threshold:
        return [float("inf"), None]
    possiblePaths = set()
    ucityList[x] = -1
    # legalNeighbors returns a list of VERTICES able to be visited
    for v in legalNeighbors(x, xColor, currColorCnt, rCount, bCount, ucityList, adjMatrix, colorArray, pathSoFar):
        pathSoFarCopy = copy.deepCopy(pathSoFar)
        lmao = visit(adjMatrix, v, threshold, ucityList, pathLength + adjMatrix[x][v])
        theWeight = lmao[0]
        thePath = pathSoFarCopy.extend(lmao[1])
        possiblePaths.add(lmao)

    res = min(possiblePaths, cmp=lambda x, y: cmp(x[0], y[0]))
    return res

def legalNeighbors(currCity, currColor, currColorCnt, rCount, bCount, ucityList, adjMatrix, colorArray, routeTrack):
    legals = []
    # pop items off of ucityList as you go.
    ucityList[currCity] = -1
    for i in range(0, len(ucityList)):
        if uCityList[i] == -1 or uCityList[i] < 0 \
        or (colorArray[ucityList[i]] == currColor and colorCnt >= 3) \
        or (colorArray[ucityList[i]] == 'R' and ((len(adjMatrix)/2) - rCount)*3 < ((len(adjMatrix)/2) - bCount) and ((len(adjMatrix)/2) - rCount) != 0) \
        or (colorArray[ucityList[i]] == 'B' and ((len(adjMatrix)/2) - bCount)*3 < ((len(adjMatrix)/2) - rCount) and ((len(adjMatrix)/2) - bCount) != 0):
            continue
        else:
            legals.append(i)
    return legals


# class UnionFind:

#     def __init__(self, adjMatrix):
#         self.adjMatrix = adjMatrix
#         self.parents = {}
#         self.ranks = {}


#     def makeSet(vertex):
#         self.parents[vertex] = vertex
#         self.ranks[vertex] = 0

#     def findSet(vertex):
#         if self.parents[vertex] != vertex:
#             self.parents[vertex] = self.findSet(self.parents[vertex])
#         return self.parents[vertex]

#     def union(v1, v2):
#         root1 = findSet(v1)
#         root2 = findSet(v2)
#         if root1 == root2:
#             return

#         # v1 and v2 are not already in the same set. Merge them.
#         if self.ranks[root1] < self.ranks[root2]:
#             self.parents[root1] = root2
#         elif self.ranks[root1] > self.ranks[root2]:
#             self.parents[root2] = self.parents[root1]
#         else
#             self.parents[root2] = root1
#             self.ranks[root1] += 1




# def kruskal(G):
#     """Return a minimum spanning tree using kruskal's algorithm"""

#     edges = []
#     for u in G:
#         for v in G[u]:
#             edges.append((u, v, G[u][v]))

#     edges.sort(cmp=lambda x,y: cmp(x[2], y[2]))

#     UF = UnionFind(G)
    
#     MST = set()
#     for u, v, d in edges:
#         setu = UF.find(u)
#         setv = UF.find(v)

#         if setu != setv:
#             MST.append((u,v))
#             UF.union(setu, setv)

#     return MST






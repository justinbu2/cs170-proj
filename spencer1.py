import sys
from itertools import permutations
import os
import glob

def allSolutions (cityNum, adjMatrix, colorArray):

	minRoute = [sys.maxint,[]];
	cities = []

	for i in range(0, cityNum):
		cities.append(i)

	var_all = list(permutations(cities))

	valids = []

	for perm in var_all:

		perm_list = [i for i in perm]
		j = len(perm_list)
		w = 0
		color_count = 0
		prev_color = colorArray[perm_list[0]]
		good_perm = True

		while (w < j):
			
			if colorArray[perm_list[w]] == prev_color:

				color_count = color_count + 1
				if color_count == 4:
					good_perm = False
					break

			else:
				color_count = 1

			w = w + 1

		if good_perm:
			valids.append(perm_list)

	for perm in valids:

		j = len(perm)
		w = 0
		cost = 0

		while w < (j - 1):

			cost = cost + adjMatrix[perm[w]][perm[w+1]]

			w = w + 1

		if cost < minRoute[0]:
			
			minRoute = [cost, perm]


	return minRoute
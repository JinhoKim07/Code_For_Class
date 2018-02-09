#!/usr/bin/python
#coding: utf-8

########## CODE DESCRIPTION ##########
# 1. File_name : Generator_RN.py
# 2. Clustering coefficient of Erodos-Renyi Model 
# 3. Result form : Clustering coefficient
# 4. ./Clustering_RN.py Nsize meank
######################################

import sys
import random

N = sys.argv[1]
meank = sys.argv[2]
total_connection = float(N) * float(meank);

N = int(N);
meank = float(meank)
rnd = random.random()
rnd_int = random.randrange(1,10)

Network = []
Degree  = []

for x in range(N):
	Degree.append(0)
	Network.append([])

count = 0

##### Make Network #####
while count < total_connection:

	while 1:
		node1 = random.randrange(0,N)
		node2 = random.randrange(0,N)

		if node1 == node2 : continue

		check_doublelink = -1

		for x in range(Degree[node1]):
			if Network[node1][x] == node2: check_doublelink = 1;

		if check_doublelink == -1 : break


	Network[node1].append(node2)
	Network[node2].append(node1)
	Degree[node1] += 1
	Degree[node2] += 1

	count += 2 

##### Clutering Coefficient #####

CC = 0.
for node in range(N):
	pair 	= 0.
	triplet	= 0.

	pair = Degree[node]*(Degree[node]-1)/2.

	for l1 in range(Degree[node]):
		neighbor = Network[node][l1]
		for l2 in range(l1, Degree[node]):
			target = Network[node][l2]
			if (target in Network[neighbor]):
				triplet += 1
	if (pair != 0):
		#print "%d\t%d\t%f" % (pair,triplet,triplet/pair)
		CC += triplet/pair

CC /= float(N)
print "%f" % (CC)

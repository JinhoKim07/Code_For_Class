#!/usr/bin/python
#coding: utf-8

########## CODE DESCRIPTION ##########
# 1. File_name : Generator_RN.py
# 2. P(k)-distributino of Erodos-Renyi Model 
# 3. Result form : k, p(k)
# 4. ./Generator_RN.py Nsize meank
######################################

import sys
import random

N = sys.argv[1]
meank = sys.argv[2]
total_connection = float(N) * float(meank);

N = int(N);
meank = float(meank)

##### INTIALIZE #####
Network = []
Degree  = []
Pk = []

for x in range(N):
	Degree.append(0)
	Network.append([])
	Pk.append(0)

count = 0

##### MAKE NETWORK #####

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


##### PRINT PK DISTRIBUTION #####

for x in range(N):
	Pk[Degree[x]] += 1

for x in range(N):
	if Pk[x] > 0 : 
		temp_degree = float(Pk[x])/float(N)
		print str(x) +"\t"+ str(temp_degree)





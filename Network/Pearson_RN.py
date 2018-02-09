#!/usr/bin/python
#coding: utf-8

########## CODE DESCRIPTION ##########
# 1. File_name : Pearson_RN.py
# 2. Find Perason Coefficient value of ER Network 
# 3. Result form : Pearson coefficient
# 4. ./Pearson_RN.py Nsize meank
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

##### Network Code #####

total_link = 0;
mean1 = 0.;
mean2 = 0.;
mean3 = 0.;

for x in range(N):
	for y in range(Degree[x]):
		mean1 += float(Degree[x]) * float(Degree[Network[x][y]])
		mean2 += (float(Degree[x]) + float(Degree[Network[x][y]]))/2.;
		mean3 += (float((Degree[x]*Degree[x])) + float((Degree[Network[x][y]]*Degree[Network[x][y]])))/2.;
	total_link += Degree[x]
	
mean1 /= float(total_link)
mean2 /= float(total_link)
mean3 /= float(total_link)

Person = (mean1-(mean2*mean2))/(mean3-(mean2*mean2))

print "%f"%(Person)

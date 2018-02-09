#!/usr/bin/python
#coding: utf-8

########## CODE DESCRIPTION ##########
# 1. File_name : NN_RN.py
# 2. 2nd nearest neighbor distribution
# 3. k_nn, p(k_nn)
# 4. ./NN_RN.py Nsize meank
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


Ave = 0.
for node in range(N):
	temp = 0.;
	
	for nn_cho in range(Degree[node]):
		nn = Network[node][nn_cho]
		temp += float(Degree[nn])/float(Degree[node])

	Ave += temp/float(N)




#print "%d\t%f"%(x,float(pk_nn[x])/float(pk_count[Degree[node]]))
print "%f"%(Ave)
#print "%d\t%f"%(x,float(pk_nn[x]))


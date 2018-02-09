#!/usr/bin/python
#coding: utf-8

########## CODE DESCRIPTION ##########
# 1. File_name : Burning_RN.py
# 2. Node to Node distance, Find Cluster using Burning Algorithm 
# 3-1. Result form (1) : Distance d, p(d)
# 3-2. Result form (2) : Clustersize n, p(n)
# 4. ./Burning_RN.py Nsize meank
######################################

import sys
import random

N = sys.argv[1]
meank = sys.argv[2]
total_connection = float(N) * float(meank);

N = int(N);
meank = float(meank)

Network = []
Degree  = []
Pk = []

for x in range(N):
	Degree.append(0)
	Network.append([])
	Pk.append(0)

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
	

### Burning Algorithm ###

Stack		= [] # Node Stack.
Distance	= [] # Node to Node distance, from initial node to other node.
Cluster		= [] # Cluster number
Clustersize	= [] # Clustersize, Clustersize[1] = 3 -> 1st cluster has 3 nodes.

ncl = -1

for x in range(N):
	Cluster.append(-1)
	Distance.append(-1)
	Clustersize.append(0)
	Stack.append(-1)

ncl = -1
init = 0
for init in range(N):
	if Cluster[init] == -1 :	# If node belongs any cluster, pass this process.
		ncl += 1 				# add 1 for cluster number.
		Cluster[init] = ncl		# assign cluster number for node.
		Clustersize[ncl] = 1;	# add 1 for "ncl"th clustersize.

		Stack[0] = init
		Distance[init] = 0

		rs = 0;					# Initialize stack address.
		ls = 1;					# Initialize legnth of Stack.
		
		while rs!=ls :			# Stack legnth == Stack address -> no more candidate node for "ncl"-th cluster.
			i = Stack[rs]		
			for num_nn in range(Degree[i]) : 	# find nearest neghibor(nn) of node i
				nn = Network[i][num_nn]			
				if Cluster[nn] == -1 :			
					Cluster[nn] = ncl
					Clustersize[ncl] += 1
					Distance[nn] = Distance[i] + 1
					Stack[ls] = nn
					ls += 1
			rs += 1


##### Distance distribution #####
"""
D_dist = []
for x in range(N):
	D_dist.append(0)

count = 0
for x in range(N):
	if(Distance[x] != -1 ): 
		D_dist[Distance[x]] += 1
		count += 1

for x in range(1,N):
	if (D_dist[x] != 0) :  print str(x) +"\t" + str(float(D_dist[x])/float(count))

"""
##### Clustersize distribution #####

dist_size=[]
for x in range(N+1):
	dist_size.append(0)

for x in range(ncl+1) :
	dist_size[Clustersize[x]] += 1

for x in range(N+1):
	if (dist_size[x] != 0) :
		print str(x) + "\t" + str(float(dist_size[x])/float(ncl+1))


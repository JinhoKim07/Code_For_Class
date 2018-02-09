#!/usr/bin/python
#coding: utf-8

########## CODE DESCRIPTION ##########
# 1. File_name : Burning_BA.py
# 2. Node to Node distance, Find Cluster using Burning Algorithm 
# 3-1. Result form (1) : Distance d, p(d)
# 3-2. Result form (2) : Clustersize n, p(n)
# 4. ./Burning_BA.py Nsize meank
######################################

import sys
import random

N = sys.argv[1]
meank = sys.argv[2]

N = int(N)
meank = int(meank)

tot_degree = 0
node_check = 0

Degree = []
Network = []
Prob = []
for x in range(N):
	Degree.append(0)
	Network.append([])
	Prob.append(0.)

##### Make initial SEED #####

for target_node in range(meank):
	
	node_check += 1
	for neighbor in range(meank):
		if (target_node == neighbor): continue
		Network[target_node].append(neighbor)
		Degree[target_node] += 1
		tot_degree += 1
		

##### preperential attacthment #####

while node_check < N:

	##### update probability #####
	for x in range(node_check):
		Prob[x] = float(Degree[x]+1.) / float(tot_degree+1.*node_check)

	new_node = node_check
	degree_check = meank
	rest_prob = 1.

	while degree_check != 0:
		prob_tot = 0.
		node_prob = random.random() * rest_prob
		for select_node in range(node_check):
			prob_tot += Prob[select_node]
			if (node_prob < prob_tot):
				Network[new_node].append(select_node)
				Network[select_node].append(new_node)
				Degree[new_node] += 1
				Degree[select_node] += 1
				rest_prob -= Prob[select_node]
				Prob[select_node] = 0.
				degree_check -= 1
				tot_degree += 2
				break

	node_check += 1


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


##### Clustersize distribution #####
"""
dist_size=[]
for x in range(N+1):
	dist_size.append(0)

print "Clustersize_distribution"
for x in range(ncl+1) :
	dist_size[Clustersize[x]] += 1

for x in range(N+1):
	if (dist_size[x] != 0) :
		print str(x) + "\t" + str(dist_size[x])
"""

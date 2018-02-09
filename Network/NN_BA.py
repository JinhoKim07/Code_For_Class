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

#!/usr/bin/python
#coding: utf-8

########## CODE DESCRIPTION ##########
# 1. File_name : Pearson_BA.py
# 2. Find Perason Coefficient value of BA Network 
# 3. Result form : Pearson coefficient
# 4. ./Pearson_BA.py Nsize meank
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

#!/usr/bin/python
#coding: utf-8

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


### Burning Algorithm ###

Stack		= [] 
Distance	= [] 
Cluster		= [] 
Clustersize	= [] 

Weight 		= [] #Assiging weight
BC			= []
modif_BC	= []
ncl = -1

for x in range(N):
	Cluster.append(-1)
	Distance.append([])
	Clustersize.append(0)
	Stack.append(-1)

	Weight.append([]) # Weight array initialize.
	BC.append([])
	modif_BC.append(0.)

	for y in range(N):
		Distance[x].append(-1)
		Weight[x].append(0) # Weight array initialize.
		BC[x].append(1.)

for init in range(N):
	
	TempNetwork = [] #Temporary network
	TempDegree	= [] #Temporary degree

	for x in range(N):
		Cluster[x] = -1
		Clustersize[x] = 0
		Stack[x] = -1

		TempNetwork.append([]) 
		TempDegree.append(0)
		
	ncl = -1
	
	if Cluster[init] == -1 :
		ncl += 1 			
		Cluster[init] = ncl		
		Clustersize[ncl] = 1;	
		Stack[0] = init
		Distance[init][init] = 0

		Weight[init][init] = 1 	# Assign vertex s distance zero, to indicate that it is zero step
								# from itself and set d. Also assign s a weight w_s = 1
		rs = 0;					
		ls = 1;					
		
		while rs!=ls :			
			i = Stack[rs]		
			for num_nn in range(Degree[i]):
				nn = Network[i][num_nn]			
				
				if Cluster[nn] == -1 :
					Cluster[nn] = ncl
					Clustersize[ncl] += 1
					
					# If j has not yet been assigned a distance, 
					# assign it distance d+1 and weight w_j = w_i	
					
					Distance[init][nn] = Distance[init][i] + 1
					Weight[init][nn] = Weight[init][i]
					
					Stack[ls] = nn
					ls += 1
				
					TempNetwork[nn].append(i)
					TempDegree[nn] += 1

				else: # If j has already assigned a distance

					if (Distance[init][nn] == Distance[init][i] + 1): 
						# And that distance is equal to d+1,
						# then the vertex's weight is icreased by w_i

						Weight[init][nn] += Weight[init][i]
						
						TempNetwork[nn].append(i)
						TempDegree[nn] += 1

			rs += 1
	else :
		print "Something wrong. maybe initialize problem"

	

	Order = []
	for x in range(N-1,-1,-1):
		Order.append(Stack[x])
	

	for x in range(N):
		root = Order[x]
		#print "root : %d" % (root)
		for nn_cho in range(0,TempDegree[root],1):
			#print "nn_cho : %d" % (nn_cho)
			nn = TempNetwork[root][nn_cho]
			BC[init][nn] += float(BC[init][root])*float(Weight[init][nn])/float(Weight[init][root])

	for x in range(N):
		modif_BC[x] += BC[init][x]
	




#LAST LINE OF Burning.
ncl += 1

for x in range(N):
	rBC = 0.5*(1.+modif_BC[x])
	print "%d\t%f"%(x,float(rBC/N))

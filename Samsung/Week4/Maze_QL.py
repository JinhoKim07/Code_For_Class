
#!/usr/bin/python

import sys
import math
import random
import copy

gamma = 0.7 # discount factor


L = 5

Maze = [[0,0,0,1,0],
	    [0,1,0,0,0],
	    [0,1,1,1,0],
	    [0,0,0,1,1],
	    [1,1,0,0,0]]
"""
L = 7

Maze = [[0,0,0,0,0,0,0],
	    [1,0,1,0,0,1,0],
	    [1,0,0,1,0,1,0],
	    [1,1,0,1,1,0,0],
	    [0,0,0,0,0,1,0],
	    [0,1,1,1,1,1,0],
	    [0,0,0,0,0,0,0]]
"""

Network 	= []
Player 		= 0
Target 		= L*L-1
Trap 		= L-1
Q_table		= []
Reward		= []
l_rate		= 1.0
gamma		= 0.7
r_target	= 100.
r_trap		= -100.



def MakeNetwork(L):

	for x in range (L*L):
		Network.append([])

	for x in range(L):
		for y in range(L):
			num = x*L + y

			if (y != 0 and Maze[x][y-1] == 0):
				Network[num].append(num-1)

			if (y%L != L-1 and Maze[x][y+1] == 0):
				Network[num].append(num+1)

			if (x != 0 and Maze[x-1][y] == 0):
				Network[num].append(num-L)

			if (x != L-1 and Maze[x+1][y] == 0):
				Network[num].append(num+L)

def print_info():

	s = ""

	px = Player % L
	py = Player / L

	ox = L-1
	oy = L-1

	for x in range(L):
		for y in range (L):
			if ([x,y] == [py,px]):
				s= s+ "P "
				continue
			elif ([x,y] == [oy,ox]):
				s= s+ "O "
				continue
			elif ([x,y] == [0,L-1]):
				s= s+ "X "
				continue
			else :
				if (Maze[x][y] == 0):
					s = s+ "- "
				else:
					s = s+ "+ "
		s= s+ "\n"

	return s

def Prob():

	s = ""

	px = Player % L
	py = Player / L

	ox = 4
	oy = 4

	for x in range(L):
		for y in range (L):

			maxv = max(Q_table[x*L+y])
			for i in range(len(Q_table[x*L+y])):
				if (maxv == Q_table[x*L+y][i]):
					maxadd = i

			direc = ""
			if (Network[x*L+y][maxadd] == x*L+y-1):
				direc = "L"
			elif(Network[x*L+y][maxadd] == x*L+y+1):
				direc = "R"
			elif(Network[x*L+y][maxadd] == x*L+y-L):
				direc = "U"
			elif(Network[x*L+y][maxadd] == x*L+y+L):
				direc = "D"
			else:
				print "something wrong."
				
			if ([x,y] == [py,px]):
				s= s+ "%.1f(%s)\t"%(maxv,direc)
				continue
			elif ([x,y] == [oy,ox]):
				s= s+ "%.1f(%s)\t"%(maxv,direc)
				continue
			elif ([x,y] == [0,4]):
				s= s+ "%.1f(%s)\t"%(maxv,direc)
				continue
			else :
				if (Maze[x][y] == 0):
					s = s+ "%.1f(%s)\t"%(maxv,direc)
				else:
					s = s+ "+\t"
		s= s+ "\n"

	return s

def Initialize(Q_table):
	for state in range(L*L):
		Q_table.append([])
		for direc in range(len(Network[state])):
			Q_table[state].append(0.)
			if (state == Target):
				Q_table[state][direc] = r_target
			if (state == Trap):
				Q_table[state][direc] = r_trap

def Find_Next(Q_table,Network,Player,Action):

	cand_state = Network[Player][Action]
	max_Q = max(Q_table[cand_state])
	
	max_add = Q_table[cand_state].index(max_Q)
	cand_action = max_add

	if (max_Q == 0.):
		max_add = random.randrange(0,len(Network[cand_state]))
		cand_action = max_add
	
	return cand_action



MakeNetwork(L)
Initialize(Q_table)

for itr in range(101):
	Player = 0
	Action = random.randrange(0,len(Network[Player]))
	print itr
	while(1):

		if (itr == 100):
			print print_info()
			print Prob()
			raw_input()
		if (Player == Target or Player == Trap): break
		next_state = Network[Player][Action]
		next_action = Find_Next(Q_table, Network, Player, Action)
		Q_table[Player][Action] += l_rate*(gamma*Q_table[next_state][next_action]-Q_table[Player][Action])

		Player = next_state
		Action = next_action

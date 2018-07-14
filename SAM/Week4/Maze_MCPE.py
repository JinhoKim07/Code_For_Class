#!/usr/bin/python

import sys
import math
import random
import copy

Maze = [[0,0,0,1,0],
	    [0,1,0,0,0],
	    [0,1,1,1,0],
	    [0,0,0,1,1],
	    [1,1,0,0,0]]

gamma = 0.7
l_rate = 1.0
Player =[]
Object = []
Trap = [0,4]
Tragectory = []
MoveDirection = []
Q_table = []
Reward = 0

def Initialize(Q_table):

	for xp in range(5):
		Q_table.append([])
		for yp in range(5):
			Q_table[xp].append([])
			for direc in range(4):
				Q_table[xp][yp].append(1)


def print_info():

	s = ""

	for x in range(5):
		for y in range (5):
			if ([x,y] == Player):
				s= s+ "P "
				continue
			elif ([x,y] == Object):
				s= s+ "O "
				continue
			elif([0,4] == [x,y]):
				s= s+ "X "
				continue
			else :
				if (Maze[x][y] == 0):
					s = s+ "- "
				else:
					s = s+ "+ "
		s= s+ "\n"

	return s

def Move(Q_table,Player):
	
	total = 0
	
	M_Prob = []
	for x in range(4):
		value = Q_table[Player[0]][Player[1]][x]
		total = total + value
	
	move_amount = 0.0
	for x in range(4):
		value = Q_table[Player[0]][Player[1]][x]
		move_amount = move_amount + float(value) / float(total)
		M_Prob.append(move_amount)

	move = random.random()
	next = -1

	for x in range(4):
		if (move < M_Prob[x]):
			next = x
			break

	return next

def Chk_Move(move):

	if (move == 0): #Move <<
		if (Player[0] == 0):
			return -1;
		else:
			tmp = Player[0] - 1;
			if (Maze[tmp][Player[1]] == 1):
				return -1;
			Player[0] = tmp;
			return 1;

	elif (move == 1): #Move >>
		if (Player[0] == 4):
			return -1;
		else:
			tmp = Player[0] + 1;
			if (Maze[tmp][Player[1]] == 1):
				return -1;
			Player[0] = tmp;
			return 1;

	elif (move == 2): #Move up
		if (Player[1] == 0):
			return -1;
		else:
			tmp = Player[1] - 1;
			if (Maze[Player[0]][tmp] == 1):
				return -1;
			Player[1] = tmp;
			return 1;

	elif (move == 3): #Move down
		if (Player[1] == 4):
			return -1;
		else:
			tmp = Player[1] + 1;
			if (Maze[Player[0]][tmp] == 1):
				return -1;
			Player[1] = tmp;
			return 1;
	else:
		print ("Error!!!")
		sys.exit()


def Chk_Goal(Player,Reward):
	if (Player == Object):
		return 1;
	
	if (Player == Trap):
		return 2;

	else:
		Reward = Reward - 1
		return -1;

def Learning(Tragectory,MoveDirection,Object,Reward,gamma):

	chk_count = 0
	while(1):

		[xp,yp] = Tragectory[-1]
		direc = MoveDirection[-1]

		[nx,ny] = [0,0]
		if (direc == 0):
			[nx,ny]=[xp-1,yp]
		elif (direc == 1):
			[nx,ny]=[xp+1,yp]
		elif (direc == 2):
			[nx,ny]=[xp,yp-1]
		elif (direc == 3):
			[nx,ny]=[xp,yp+1]
		else:
			print "Error"

		dot_max = -1
		for x in range(4):
			if (Q_table[nx][ny][x] > dot_max):
				dot_max = Q_table[nx][ny][x]
		
		Q_table[xp][yp][direc] += l_rate*(gamma*dot_max - Q_table[xp][yp][direc])

		if (chk_count == 0):
			Q_table[xp][yp][direc] += l_rate*Reward
			chk_count += 1

		if (len(MoveDirection) < 2):
			break

		Tragectory.pop()
		MoveDirection.pop()



## Code Start 
Initialize(Q_table)
iteration = 0
	
while(1):

	Player = [0,0]
	Object = [4,4]
	Trap   = [0,4]
	
	Reward = 0
	add = copy.deepcopy(Player)
	Tragectory.append(add)
	while(1):
		
		next = Move(Q_table,Player)
		chk = Chk_Move(next)
		if (chk == -1):
			continue
		
		add = copy.deepcopy(Player)
		Tragectory.append(add)
		MoveDirection.append(next)
		
		if (iteration % 5000 ==1 and iteration > 100):
			print print_info()
			raw_input()

		goal = Chk_Goal(Player,Reward)
		if (goal == 1): 
			Reward += 50
			break
		if (goal == 2):
			Reward += -50
			break
		
	Tragectory.pop() # We does't need last objective goal

	Learning(Tragectory,MoveDirection,Object,Reward,gamma)
	Tragectory = []
	MoveDirection = []
	iteration += 1

	if (iteration % 1000 == 0): 
		print "Iteration %d done." % (iteration)

	


	

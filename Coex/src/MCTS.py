
# coding: utf-8

import src.Omok as omok
import numpy as np

class MCTS:

	L = 0
	N = L*L
	c_puct = 1.
	tau = 1.
	epsilon = 0.25

	
	def __init__(self,l,goal_n,c,t,e):
		global L
		global N
		global c_puct
		global tau
		global epsilon
		
		L = l
		N = L*L
		c_puct = c
		tau = t
		epsilon = e
		
		Game = omok.Omok(L,goal_n)

		self.Tree = []
		self.IDX = []
		self.Tree_Net =[]
		self.Nt = []
		self.Wt = []
		self.Qt = []
		self.Pt = []
		self.Trajectory = []
		self.Trajectory_A = []
		self.Policy = []
        
	def Initialize(self):
		self.Tree = []
		self.IDX = []
		self.Tree_Net =[]
		self.Nt = []
		self.Wt = []
		self.Qt = []
		self.Pt = []
		self.Trajectory = []
		self.Trajectory_A = []
		self.Policy = []


	def Whosstone(self,who):
	    if ("p1" == who):
	        stone = 1
	    else:
	        stone = 2
	    return stone


	def MCTS_SELECT (self, c_puct, current_state):
	    ### PARAMETER SETTING ###

	    # Current Board Registration on the Tree

	    p1_num = current_state.count(1)
	    p2_num = current_state.count(2)

	    if (p2_num < p1_num):
	        cand_player = "p2"
	    else:
	        cand_player = "p1"


	    # when you run this process,
	    # If the tree is empty or needs a new tree, 
	    # part of "except" will be run the except
	    # other case, find the state in the tree and append Trajectory

	    try :
	        current_idx = self.Tree.index(current_state)

	    except:
	        #IDX = [0]
	        #self.Tree = [current_state]
	        #self.Tree_Net = [[]]
	        #self.Nt = [[0 for i in range(N)]]
	        #self.Wt = [[0 for i in range(N)]]
	        #self.Qt = [[0 for i in range(N)]]
	        #self.Pt = [leaf_p]
	        #print ("except case")
	        #current_idx = self.Tree.index(current_state)
	        return []

	    self.Trajectory = [current_state]
	    self.Trajectory_A = []


	    
	    while(1):

	        ## All Tree Search Process based on the Trajectory
	        current_state = self.Trajectory[-1]
	        current_idx = self.Tree.index(current_state)

	        if (not current_state.count(0)):
	            #print ("End of the Tree")
	            return []

	        ## Select the Stone Colour
	        stone = self.Whosstone(cand_player)

	        ## Candidate Action list for all candidate
	        Cand_Action = []
	        ## Regal_move list for all candidate
	        Regal_move = []

	        ## Cadidate Action List will be produce
	        

	        for i in range(N):
	            if (current_state[i] == 0):
	                tmp = current_state.copy()
	                tmp[i] = stone
	                Regal_move.append(i)
	                
	        # Calculate Sum of N(s,b)
	        sum_N = 0
	        for nn_idx in Regal_move:
	            sum_N = sum_N + self.Nt[current_idx][nn_idx]

	        Diri_Pt = []
	        alpha = [0.03 for i in range(len(self.Pt[current_idx]))]
	        Diri_dist = np.random.dirichlet(alpha)
	        for i in range(len(self.Pt[current_idx])):
	            Diri_Pt.append((1.-epsilon)*self.Pt[current_idx][i] +
                               epsilon*Diri_dist[i])
	        # Calculate U(s,a)
	        For_argmax = []
	        for nn_idx in Regal_move:
	            tmp_p = Diri_Pt[nn_idx]
	            tmp_q = self.Qt[current_idx][nn_idx]
	            tmp_n = self.Nt[current_idx][nn_idx]
	            For_argmax.append(float(c_puct) * float(tmp_p) 
                                  * np.sqrt(sum_N) /float(1.+tmp_n) 
	                              + float(tmp_q))

	        A_t_value = max(For_argmax)
	        A_t_idx = For_argmax.index(A_t_value)
	        
	        A_t = current_state.copy()
	        A_t[Regal_move[A_t_idx]] = stone
	        self.Trajectory_A.append(Regal_move[A_t_idx])

	        try: 
	            next_idx = self.Tree.index(A_t)
	            self.Trajectory.append(A_t)
	            if (cand_player == "p1"):
	                cand_player = "p2"
	            else:
	                cand_player = "p1"

	        except:
	            #print ("break")
	            break

	    return A_t


	def MCTS_EXPAND(self,A_t,leafp,leafv):
	  
	  	## EXPAND AND EVALUATE
		leaf_state = A_t.copy()
		self.IDX.append(len(self.Tree))
		self.Tree.append(leaf_state.copy())
		self.Tree_Net.append([])

	    
		if (self.Trajectory):
			prev_state = self.Trajectory[-1]
			prev_idx = self.Tree.index(prev_state)
			self.Tree_Net[prev_idx].append(self.IDX[-1])

		leaf_p = leafp
		leaf_v = leafv

		self.Pt.append(leaf_p.copy())
		self.Nt.append([0 for i in range(N)])
		self.Wt.append([0 for i in range(N)])
		self.Qt.append([0 for i in range(N)])

		return leaf_v



	def MCTS_BACKUP(self,leaf_v,A_t):

	    ## BACK UP

	    self.Trajectory.reverse()
	    self.Trajectory_A.reverse()

	    i = 0
	    a_idx = -1
	    for prev,a_idx in zip(self.Trajectory,self.Trajectory_A):

	        idx = self.Tree.index(prev)

	        self.Nt[idx][a_idx] = self.Nt[idx][a_idx]+1
	        self.Wt[idx][a_idx] = self.Wt[idx][a_idx]+leaf_v
	        self.Qt[idx][a_idx] = self.Wt[idx][a_idx]/self.Nt[idx][a_idx]
	        
	        i = i+1


	def MCTS_PLAY (self,tau,current_state):
	    

	    #current_state = Game.Board.copy()
	    current_idx = self.Tree.index(current_state)

	    sum_N = 0
	    for idx in range(N):
	        sum_N = sum_N + self.Nt[current_idx][idx]

	    best_cand = -1
	    BEST_IDX = -1
	    
	    self.Policy = []
	    self.Proport = []
	    for idx in range(N):    
	        if (self.Nt[current_idx][idx] != 0):
	            policy_value = np.power(self.Nt[current_idx][idx],1/tau) / np.power(sum_N,1/tau)
	            self.Policy.append(policy_value)
	        else:
	            self.Policy.append(1)
	                
	    #print(current_state)
	    #print(Policy)
	    tmp = []
	    for idx in range(N):
	    
	        if (current_state[idx] == 0):
	            if (self.Policy[idx] == 0):
	                tmp.append(0)
	            else:
	                #self.Proport.append(self.Policy[idx])
	                tmp.append(self.Policy[idx])
	        else:
	            #self.Proport.append(0)
	            tmp.append(0)
	                
	    tmp_sum = sum(tmp)
	    self.Proport = [value/tmp_sum for value in tmp]
	    for i in range(1,N):
	        self.Proport[i] = self.Proport[i]+self.Proport[i-1]
	    #print(Proport)
	    
	    selector = np.random.rand()
	    #print (selector)
	    cand_action = -1
	    
	    for idx in range(N):
	        if (selector < self.Proport[idx]):
	            cand_action = idx
	            break
	    #print (cand_action)

	    #####
	    ## ADD the probability of prportionally 
	    #####
	    
	    now_player = ""
	    x = -1
	    y = -1

	    np1 = current_state.count(1)
	    np2 = current_state.count(2)
	    
	    if np1 <= np2:
	        now_player = "p1"
	    else:
	        now_player = "p2"
	        
	    x = cand_action % L
	    y = cand_action // L
	    
	    return now_player, x, y
	    
	    ## Add Resign Rate

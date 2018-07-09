
# coding: utf-8

class Omok:

    L = 0

    def __init__(self,l,goal_n):
        global L
        global goal
        L = l
        goal = goal_n
        self.Board = []
        

    def Initialize(self):
        global Network
        global N

        N = L*L
        self.Board = [0 for i in range(N)]
        Network = [[0] for i in range(N)]
        self.MakeNetwork()

    def MakeNetwork(self):
        global Network
        
        for pos in range(L*L-1):

            if ((pos+1) % L == 0): #right side on the Network
                Network[pos][0] = Network[pos][0] + 2
                Network[pos+L][0] = Network[pos+L][0] + 1
                Network[pos+L-1][0] = Network[pos+L-1][0] + 1
                Network[pos].append(pos+L)
                Network[pos].append(pos+L-1)
                Network[pos+L].append(pos)
                Network[pos+L-1].append(pos)
     
            elif (pos >= (L*(L-1))): # Bottom side on the Network
                Network[pos][0] = Network[pos][0] + 1
                Network[pos+1][0] = Network[pos+1][0] + 1
                Network[pos].append(pos+1)
                Network[pos+1].append(pos)
                
            elif (pos % L == 0):
                Network[pos][0] = Network[pos][0] + 3
                Network[pos+1][0] = Network[pos+1][0] + 1
                Network[pos+L][0] = Network[pos+L][0] + 1
                Network[pos+L+1][0] = Network[pos+L+1][0] + 1
                Network[pos].append(pos+1)
                Network[pos].append(pos+L)
                Network[pos].append(pos+L+1)
                Network[pos+1].append(pos)
                Network[pos+L].append(pos)
                Network[pos+L+1].append(pos)
            
            else:       
                Network[pos][0] = Network[pos][0] + 4
                Network[pos+1][0] = Network[pos+1][0] + 1
                Network[pos+L][0] = Network[pos+L][0] + 1
                Network[pos+L-1][0] = Network[pos+L-1][0] + 1
                Network[pos+L+1][0] = Network[pos+L+1][0] + 1
                Network[pos].append(pos+1)
                Network[pos].append(pos+L)
                Network[pos].append(pos+L-1)
                Network[pos].append(pos+L+1)
                Network[pos+1].append(pos)
                Network[pos+L].append(pos)
                Network[pos+L-1].append(pos)
                Network[pos+L+1].append(pos)
            
            

    def PrintBoard(self):
        global L

        for i in range(L):
            for j in range(L):
                pos = i*L + j
                ops = "-"
                if (self.Board[pos]==1):
                    ops = "O"
                if (self.Board[pos]==2):
                    ops = "X"

                print (ops,end=" ")

            print ("")
                
    def Playing(self,agent,x,y):

        global L

        pos = x + y*L
        res = -1

        if (self.Board[pos] != 0):
            #print (x,y," is Another Stone on the Board")
            return 0

        if (agent == "p1"):
            res = 1
        elif (agent == "p2"):
            res = 2
        else:
            print ("Error")
            return 0

        self.Board[pos] = res
        return 1

    def BFF_Bingo(self,agent):
        global Network
        self.Board
        global N
        global goal
        
        if (agent == "p1"):
            stone = 1
        if (agent == "p2"):
            stone = 2
        
        for start in range(N):

            match = 0

            for i in range(goal):
                if (self.Board[start+i] == stone):
                    match = match + 1
                    
                if (match == goal):
                    return True
                
                if ((start+i+1)%L == 0):
                    break



            match = 0

            for i in range(goal):

                if (self.Board[start+L*i] == stone):
                    match = match + 1
                    
                if (match == goal):
                    return True
                
                if (start+(L)*(i+1) > N-1):
                    break


            match = 0

            for i in range(goal):
                
                if (self.Board[start+(i+(L*i))] == stone):
                    match = match + 1
                if (match == goal):
                    return True 
                if (start+(L*(i+1)) > N-1) or ((start+i+1)%L == 0) :
                    break
                
            match = 0

            for i in range(goal):
                if (self.Board[start+(L*i)-i] == stone):
                    match = match + 1
                if (match == goal):
                    return True
                if (start+(L*(i+1)) > N-1) or ((start-i)%L == 0) :
                    break



                
        return False


    def PlayforPlayer(self):
        Player = "p1"
        self.Board = [0 for i in range(L*L)]
        self.MakeNetwork()
        process = 1

        while (process):
            x = input(Player+" input x : ")
            y = input(Player+" input y : ")
            x = int(x)
            y = int(y)
            chk = self.Playing(Player,x,y)
            
            if (not chk): continue
            
            self.PrintBoard()
            Length = self.BFF_Bingo(Player)
            #print (Length)
            if (Length >=4 ):
                print(Player, "win")
                process = 0
            
            if (Player == "p1"):
                Player = "p2"
            else:
                Player = "p1"


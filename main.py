import math
import random
import copy

class NPuzzle:
    def __init__(self,board,goal):
        self.board = board
        self.goal = goal
        self.child = []
        self.parent = ""
    def setBoard(self,board):
        self.board = board
    def setGoal(self,goal):
        self.goal = goal
    #def __init__(self, board, goal):
    #    self.board = board
    #    self.goal = goal
    
    def isGoal(self):
        if self.board == self.goal:
            return True
        else:
            return False

    def getBoard(self):
        return copy.deepcopy(self.board)
    def getGoal(self):
        return copy.deepcopy(self.goal)

#################################
# NPUZZLE PROBLEM
#################################
def initNBoard(n):
    length = int(math.sqrt(n))
    start = 1
    arr = [[0 for i in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            arr[i][j] = start
            start = start + 1
    arr[length-1][length-1] = "X"
    return arr

def findMark(arr):
    column = ''
    row = ''
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == "X":
                column = j
                row = i
    return (row,column)

def shuffleBoard(arr):
    for x in range(50):
        pos = findMark(arr)
        direction = random.randint(0,3)
        #up
        if direction == 0:
            if pos[0]-1 < 0:
                continue
            else:
                temp = arr[pos[0] -1 ][pos[1]]
                arr[pos[0] -1 ][pos[1]] = "X"
                arr[pos[0]][pos[1]] = temp
        #down
        if direction == 1:
            if pos[0]+1 > len(arr) -1:
                continue
            else:
                temp = arr[pos[0] +1 ][pos[1]]
                arr[pos[0] +1 ][pos[1]] = "X"
                arr[pos[0]][pos[1]] = temp
        #left 
        if direction == 2:
            if pos[1]-1 < 0:
                continue
            else:
                temp = arr[pos[0]][pos[1]-1]
                arr[pos[0]][pos[1]-1] = "X"
                arr[pos[0]][pos[1]] = temp   
        #right 
        if direction == 3:
            if pos[1]+1 > len(arr)-1:
                continue
            else:
                temp = arr[pos[0]][pos[1]+1]
                arr[pos[0]][pos[1]+1] = "X"
                arr[pos[0]][pos[1]] = temp
    return arr

def movePOS(num, arry):
    pos = findMark(arry)
    arr = copy.deepcopy(arry)
    direction = num
    #up
    if direction == 0:
        if pos[0] -1 < 0:
            return []
        else:
            temp = arr[pos[0] -1 ][pos[1]]
            arr[pos[0] -1 ][pos[1]] = "X"
            arr[pos[0]][pos[1]] = temp
    #down
    if direction == 1:
        if pos[0]+1 > len(arr) -1:
            return [] 
        else:
            temp = arr[pos[0] +1 ][pos[1]]
            arr[pos[0] +1 ][pos[1]] = "X"
            arr[pos[0]][pos[1]] = temp
    #left 
    if direction == 2:
        if pos[1]-1 < 0:
            return []
        else:
            temp = arr[pos[0]][pos[1]-1]
            arr[pos[0]][pos[1]-1] = "X"
            arr[pos[0]][pos[1]] = temp
    #right 
    if direction == 3:
        if pos[1]+1 > len(arr)-1:
            return []
        else:
            temp = arr[pos[0]][pos[1]+1]
            arr[pos[0]][pos[1]+1] = "X"
            arr[pos[0]][pos[1]] = temp
    return copy.deepcopy(arr)
       
def expandNodes(arr,goal):
    up = NPuzzle(movePOS(0,copy.deepcopy(arr)),goal)
    down = NPuzzle(movePOS(1,copy.deepcopy(arr)),goal)
    left = NPuzzle(movePOS(2,copy.deepcopy(arr)),goal)
    right =  NPuzzle(movePOS(3,copy.deepcopy(arr)),goal)
    return [copy.deepcopy(up),copy.deepcopy(down),copy.deepcopy(left),copy.deepcopy(right)]


goal = initNBoard(4)
board = shuffleBoard(initNBoard(4))

npuzzle = NPuzzle(board,goal)
arr = npuzzle.getBoard()
print("Starting array:\n"+str(arr))

print("goal:\n"+str(npuzzle.getGoal())+"\n")
queue = []
states = []
def graphSearch(puzzle, search, queue, states):
    if search == "bf":
        if puzzle.isGoal():
            return puzzle
        else:
            print("current"+str(puzzle.getBoard()))
            states.append(copy.deepcopy(puzzle.getBoard()))
            explore = expandNodes(copy.deepcopy(npuzzle.getBoard()),npuzzle.getGoal())
            for i in copy.deepcopy(explore): 
                if not i.getBoard():
                    continue
                puzzle.child.append(i)
                i.parent = puzzle
                if copy.deepcopy(i.getBoard()) not in copy.deepcopy(states):
                    print(i.getBoard())
                    queue.append(copy.deepcopy(i))
            
            try:
                x = queue.pop(0)
            except:
                x = False
            if x:
                graphSearch(copy.deepcopy(x), "bf", queue,states)

print(graphSearch(npuzzle, "bf", queue, states))
            

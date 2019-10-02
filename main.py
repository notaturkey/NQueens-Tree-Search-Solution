import math
import random
import copy

class NPuzzle:
    def __init__(self,board,goal):
        self.board = board
        self.goal = goal
        self.child = []
        self.parent = ""
        self.depth = 0
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

def graphSearch(search, queue, states):
    global depth
    if search == "bf":
        if queue:
            while queue:
                for i in queue:
                    if i.isGoal():
                        return i
                parent = queue.pop(0)    
                states.append(copy.deepcopy(parent.getBoard()))
                explore = expandNodes(copy.deepcopy(parent.getBoard()),parent.getGoal())
                depth = depth +1
                for i in copy.deepcopy(explore): 
                    if not i.getBoard():
                        continue
                    parent.child.append(i)
                    i.parent = parent
                    if copy.deepcopy(i.getBoard()) not in copy.deepcopy(states):
                        i.depth = depth
                        queue.append(copy.deepcopy(i))
    if search == "df":
        if queue:
            while queue:
                current = queue.pop(0)
                # if current.depth > 300:
                #     continue
                states.append(current.getBoard())
                if current.isGoal():
                    return current
                else:
                    depth = depth + 1
                    explore = expandNodes(copy.deepcopy(current.getBoard()),current.getGoal())
                    for i in copy.deepcopy(explore):
                        i.depth = depth
                        current.child = i 
                        i.parent = current
                        if i.getBoard():
                            if i.getBoard() not in states:
                                queue.append(i)

goal = initNBoard(9)
board = shuffleBoard(initNBoard(9))
npuzzle = NPuzzle(board,goal)
arr = npuzzle.getBoard()
print("Starting array:\n"+str(arr))
print("goal:\n"+str(npuzzle.getGoal())+"\n")
queue = []
states = []
depth = 0
queue.append(npuzzle)
result=""
#result = graphSearch("bf", queue, states)
print("Path is:")
if result:           
    while True:
        print(result.board)
        if result.parent:
            result = result.parent
        else:
            break
else:
    print("didnt find with maximum depth = 300")
npuzzle = NPuzzle(board,goal)
arr = npuzzle.getBoard()
print("Starting array:\n"+str(arr))
print("goal:\n"+str(npuzzle.getGoal())+"\n")
queue = []
states = []
queue.append(npuzzle)
# depth = 0
#result = graphSearch("df", queue, states)
print("Path is:")
if result:           
    while True:
        print(result.board)
        if result.parent:
            result = result.parent
        else:
            break
else:
    print("didnt find with maximum depth = 300")

###############################################
# NQUENNS YAY
################################################

class NQueen:
    def __init__(self,board):
        self.board = board
        self.goal = goal
        self.child = []
        self.parent = ""
        self.depth = 0
    def setBoard(self,board):
        self.board = board
    #def __init__(self, board, goal):
    #    self.board = board
    #    self.goal = goal   
    def isGoal(self,pos):
        for i in pos:
            for x in range(len(pos)):
                if i[0] in pos[x][0]:
                    return False
                elif i[1] in pos[x][1]:
                    return False
            for x in pos: 
                if i==x:
                    continue
                if abs(x[1] - i[1] / x[0] - i[0]) == 1:
                    return False
        return True


    def getBoard(self):
        return copy.deepcopy(self.board)
    def getGoal(self):
        return copy.deepcopy(self.goal)

def initQBoard(n):
    length = int(math.sqrt(n))
    arr = [[0 for i in range(length)] for i in range(length)]
    for i in arr:
        i[0] = "X"
    return arr

def findQMark(arr):
    column = ''
    row = ''
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == "X":
                column = j
                row = i
                result.append([column,row])
    return result
print(str(findQMark(board)))

def moveQ(col, direction, arry):
    pos = findQMark(arry)
    row = pos[col][0]
    arr = copy.deepcopy(arry)
    #down
    if direction == 0:
        if row + 1 > len(arr):
            result = []
            return result
        else:
            temp = arr[col][row+1]
            arr[col][row+1] = "X"
            arr[col][row] = temp
    #up
    if direction == 1:
        if row - 1 < 0:
            result = []
            return result
        else:
            temp = arr[col][row-1]
            arr[col][row-1] = "X"
            arr[col][row] = temp
    return copy.deepcopy(arr)

print(str(moveQ(0,0,copy.deepcopy(board))))
def expandQNodes(arr,goal):
    count = 0
    results = []
    for i in arr:
        #up = NQueen(moveQ(count,1,copy.deepcopy(arr)),goal)
        down = NQueen(moveQ(count,0,copy.deepcopy(arr)))
        results.append(down)
        count = count + 1
    return results
print(str(expandQNodes(copy.deepcopy(board), copy.deepcopy(board))))

def graphSearchQueen(search, queue, states):
    global depth
    if search == "bf":
        if queue:
            while queue:
                for i in queue:
                    temp = i.isGoal() 
                    if i.isGoal():
                        return i
                parent = queue.pop(0)    
                states.append(copy.deepcopy(parent.getBoard()))
                explore = expandQNodes(copy.deepcopy(parent.getBoard()),parent.getGoal())
                depth = depth +1
                for i in copy.deepcopy(explore):
                    if not i.getBoard():
                        continue
                    parent.child.append(i)
                    i.parent = parent
                    if copy.deepcopy(i.getBoard()) not in copy.deepcopy(states):
                        i.depth = depth
                        queue.append(copy.deepcopy(i))
    if search == "df":
        if queue:
            while queue:
                current = queue.pop(0)
                # if current.depth > 300:
                #     continue
                states.append(current.getBoard())
                if current.isGoal():
                    return current
                else:
                    depth = depth + 1
                    explore = expandNodes(copy.deepcopy(current.getBoard()),current.getGoal())
                    for i in copy.deepcopy(explore):
                        i.depth = depth
                        current.child = i 
                        i.parent = current
                        if i.getBoard():
                            if i.getBoard() not in states:
                                queue.append(i)

                                
board = initQBoard(16)
nqueen = NQueen(board)
print("queen board:\n"+str(board))
arr = npuzzle.getBoard()
print("Starting array:\n"+str(arr))
queue = []
states = []
queue.append(nqueen)
print(str(graphSearchQueen("bf", queue, states).getBoard()))
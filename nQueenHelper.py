import math
import random
import copy

class NQueen:
    def __init__(self,board):
        self.board = board
        self.goal = []
        self.child = []
        self.parent = ""
        self.depth = 0

    def setBoard(self,board):
        self.board = board

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

def expandQNodes(arr,goal):
    count = 0
    results = []
    for i in arr:
        #up = NQueen(moveQ(count,1,copy.deepcopy(arr)),goal)
        down = NQueen(moveQ(count,0,copy.deepcopy(arr)))
        results.append(down)
        count = count + 1
    return results

def graphSearchQueen(search, queue, states):
    if search == "bf":
        if queue:
            while queue:
                for i in queue:
                    temp = i.isGoal(findQMark(i))
                    if i.isGoal(findQMark(i)):
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
                states.append(current.getBoard())
                print(current)
                if current.isGoal(findQMark(current.getBoard())):
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

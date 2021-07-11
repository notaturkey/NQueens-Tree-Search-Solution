import math
import random
import copy
from klotskiHelper import *

goal = initNBoard(9)
board = shuffleBoard(initNBoard(9))
game = Klotski(board,goal)
arr = game.getBoard()
print("Starting array:\n"+str(arr))
print("goal:\n"+str(game.getGoal())+"\n")
queue = []
states = []
depth = 0
maxDepth = 1000
queue.append(game)
result=""
print("Doing a Breadth First Search")
result = graphSearch("bf", queue, states, depth, maxDepth)
if result:
    print("Path is:")
    while True:
        print(result.board)
        if result.parent:
            result = result.parent
        else:
            break
else:
    print("didnt find with maximum depth = " + str(maxDepth))

game = Klotski(board,goal)
arr = game.getBoard()
print("Starting array:\n"+str(arr))
print("goal:\n"+str(game.getGoal())+"\n")
queue = []
states = []
queue.append(game)
depth = 0
maxDepth = 1000
print("Doing a Depth First Search")
result = graphSearch("df", queue, states, depth, maxDepth)
if result:
    print("Path is:")
    while True:
        print(result.board)
        if result.parent:
            result = result.parent
        else:
            break
else:
    print("didnt find with maximum depth = ", str(maxDepth))

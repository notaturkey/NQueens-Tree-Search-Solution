from nQueenHelper import *

board = initQBoard(16)
nqueen = NQueen(board)
print("queen board:\n"+str(board))
queue = []
states = []
queue.append(nqueen)
print(str(graphSearchQueen("df", queue, states).getBoard()))

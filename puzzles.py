class NPuzzle:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.parent= ''
        self.child= ''
        self.sampleSpace = []
    
    def isGoal(self):
        if self.board == self.goal:
            return True
        else:
            return False

    def findMark(self):
        column = ''
        row = ''
        arr = self.board
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] == "X":
                    column = j
                    row = i
        return (row,column)    
    
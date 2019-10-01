class NPuzzle:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.stateSpace = []
    
    def isGoal(self):
        if self.board == self.goal:
            return True
        else:
            return False
    
    def nextState(self, board, search):
        print()


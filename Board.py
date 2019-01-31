class Board:
    WIDTH  = 5
    HEIGHT = 5
    emptyElement = "   "

    board = [[]]

    def __init__(self, width=6, height=5):
        self.initboard(width, height)
    
    def initboard(self, width, height):
        self.WIDTH  = width
        self.HEIGHT = height
        emptyElement = self.emptyElement
        
        board = [[emptyElement for i in range(width)] for j in range(height)]
        self.board = board
        
    # Place an element in a column if possible. Return true on success
    def placeElement(self, e, column):
        if column >= self.WIDTH or column < 0:
            return False
        height = self.HEIGHT
        board  = self.board  
        
        for i in range(0, height):
            if board[i][column] == self.emptyElement:
                board[i][column] = e
                return True
        return False
    
    def printPretty(self):
        board  = self.board
        width  = self.WIDTH
        height = self.HEIGHT
        elwidth = len(board[0][0])
        
        print("-" * ((elwidth*width) + width + 1))
        for i in reversed(range(0, height)):
            print("|", end="")
            for j in range(0, width):
                print (board[i][j], end="|") 
            print()
            print("-" * ((elwidth*width) + width + 1))
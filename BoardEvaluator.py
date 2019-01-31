class BoardEvaluator:
    P1Element = ""
    P2Element = ""

    def __init__(self, P1Element, P2Element):
        self.P1Element = P1Element
        self.P2Element = P2Element
        
    
    
    def winCondition(self, playerElement, board):
        return self.checkRows(playerElement, board) or self.checkColumns(playerElement, board) or self.checkDiagonals(playerElement, board)
        
    def checkRows(self, playerElement, board):
        width  = board.WIDTH
        height = board.HEIGHT
        board  = board.board
        if width < 4:
            return False
        
        for i in range(0, height):
            counter = 0
            for j in range(0, width):
                if (board[i][j] == playerElement):
                    counter += 1
                else:
                    counter = 0
                if counter == 4:
                    return True
                    
        return False
        
    def checkColumns(self, playerElement, board):
        width  = board.WIDTH
        height = board.HEIGHT
        board  = board.board  
        if height < 4:
            return False
        
        for i in range(0, width):
            counter = 0
            for j in range(0, height):     
                if (board[j][i] == playerElement):
                    counter += 1
                else:
                    counter = 0
                if counter == 4:
                    return True
                    
        return False
        
    def checkDiagonals(self, playerElement, board):
        return False
        
        
        
        
        
        
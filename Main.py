from Board import *
from BoardEvaluator import *

class Main:
    if __name__ == "__main__":
        print("hello")
        #bm = Boardmanager()
        board = Board(width=10)
        board.printPretty()
        board.placeElement(" X ", 3)
        board.printPretty()  
        bv = BoardEvaluator(" X ", " O ")
        print(bv.winCondition(" X ", board))
        board.placeElement(" X ", 4)
        board.printPretty()  
        print(bv.winCondition(" X ", board))
        
        board.placeElement(" X ", 2)
        board.printPretty()  
        print(bv.winCondition(" X ", board))
        
        board.placeElement(" X ", 0)
        board.printPretty()  
        print(bv.winCondition(" X ", board))
        
        board.placeElement(" O ", 5)
        board.printPretty()  
        print(bv.winCondition(" X ", board))
        
        board.placeElement(" X ", 7)
        board.printPretty()  
        print(bv.winCondition(" X ", board))    

        board.board[2][3] = " X "
        board.board[2][4] = " X "
        board.board[2][5] = " X "
        board.board[2][6] = " X "
        board.printPretty()  
        print(bv.winCondition(" X ", board))  
        board.placeElement(" X ", 3)
        board.printPretty()  
        print(bv.winCondition(" X ", board))     
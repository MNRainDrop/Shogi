from Square import Square
from Piece import *
"""
This class handles all actions taken with the board.

Every Board contains an 9x9 2d array/list of Squares.
"""
class Board():
    def __init__(self) -> None:
        self.board = [[Square(i,j) for i in range(9)] for j in range(9)]
        
        # fills in the pawns
        for i in range(0,9):
            self.board[2][i].setOccupiedBy(Pawn("b"))
            self.board[6][i].setOccupiedBy(Pawn("w"))

    def printBoard(self):
        for row in self.board:
            print(*row)

def main():
    b = Board()
    b.printBoard()

if __name__ == "__main__":
    main()
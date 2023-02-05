from Square import Square
from Player import Player
from Piece import *
"""
This class handles all actions taken with the board.

Every Board contains an 9x9 2d array/list of Squares.
"""
class Board():
    def __init__(self) -> None:
        self.board = [[Square(j,i) for i in range(9)] for j in range(9)]
        self.white = Player()
        self.black = Player()
        
        # fills in the pawns
        for i in range(0,9):
            self.black.boardPieces.append(Pawn(self.board[i][2]))
            self.white.boardPieces.append(Pawn(self.board[i][6]))

        # fills in the kings
        self.black.boardPieces.append(King(self.board[4][0]))
        self.white.boardPieces.append(King(self.board[4][8]))

        # fills in the bishops
        self.black.boardPieces.append(Bishop(self.board[7][1]))
        self.white.boardPieces.append(Bishop(self.board[1][7]))

        # fills in the rooks
        self.black.boardPieces.append(Rook(self.board[1][1]))
        self.white.boardPieces.append(Rook(self.board[7][7]))

        #fills in the lances
        self.black.boardPieces.append(Lance(self.board[0][0]))
        self.black.boardPieces.append(Lance(self.board[8][0]))
        self.white.boardPieces.append(Lance(self.board[0][8]))
        self.white.boardPieces.append(Lance(self.board[8][8]))

        #fills in the knights
        self.black.boardPieces.append(Knight(self.board[1][0]))
        self.black.boardPieces.append(Knight(self.board[7][0]))
        self.white.boardPieces.append(Knight(self.board[1][8]))
        self.white.boardPieces.append(Knight(self.board[7][8]))

        #fills in the silver generals
        self.black.boardPieces.append(SilverGeneral(self.board[2][0]))
        self.black.boardPieces.append(SilverGeneral(self.board[6][0]))
        self.white.boardPieces.append(SilverGeneral(self.board[2][8]))
        self.white.boardPieces.append(SilverGeneral(self.board[6][8]))

        #fills in the gold generals
        self.black.boardPieces.append(GoldGeneral(self.board[3][0]))
        self.black.boardPieces.append(GoldGeneral(self.board[5][0]))
        self.white.boardPieces.append(GoldGeneral(self.board[3][8]))
        self.white.boardPieces.append(GoldGeneral(self.board[5][8]))

        # links the pieces to the squares
        for i in self.white.boardPieces:
            self.board[i.currentSquare.x][i.currentSquare.y].isOccupied = True
        for i in self.black.boardPieces:
            self.board[i.currentSquare.x][i.currentSquare.y].isOccupied = True
            
    '''
        Moves pieces in the board array and reassigns the current piece square
    '''
    def movePiece(self):
        pass

    '''
        Prints the Board
    '''
    def printBoard(self):
        for j in range(0,9):
            for i in range(0,9):
                # if the current square is occupied run this code
                if self.board[i][j].isOccupied:
                    
                    # for each black piece, find the piece with the current square
                    for x in self.black.boardPieces:
                        if x.currentSquare == self.board[i][j]:
                            print("b" + str(x), end=" ")

                    # for each white piece, find the piece with the current square
                    for x in self.white.boardPieces:
                        if x.currentSquare == self.board[i][j]:
                            print("w" + str(x), end=" ")
                    
                # if the current square on the board is not occupied, just print the square
                else:
                    print(self.board[i][j], end=" ")
            print()

    def __str__(self) -> str:
        self.printBoard()
        return ""

def main():
    b = Board()
    print(b)

if __name__ == "__main__":
    main()
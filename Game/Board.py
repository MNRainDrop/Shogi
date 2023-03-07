from Square import Square
from Player import Player
from Piece import *

'''
This class handles all actions taken with the board.

Every Board contains an 9x9 2d array/list of Squares.
'''
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
            self.board[i.x][i.y].isOccupied = True
        for i in self.black.boardPieces:
            self.board[i.x][i.y].isOccupied = True
            i.color = 1
    
    '''
        Gets piece at current row and column
    '''
    def getPiece(self, rows, cols, turn):
        currSquare = self.board[rows][cols]
        if turn%2 == 0:
            for pieces in self.white.boardPieces:
                if pieces.square == currSquare:
                    piece = pieces
                    pass
        else:
            for pieces in self.black.boardPieces:
                if pieces.square == currSquare:
                    piece = pieces
                    pass
        return piece

    '''
        Moves pieces in the board array and reassigns the current piece square
    '''
    def movePiece(self, rows, cols, piece):
        if self.board[rows][cols].validMove == True:
            piece.square.isOccupied = False
            self.board[rows][cols].isOccupied = True
            piece.square = self.board[rows][cols]
            piece.x = rows
            piece.y = cols
            return 1
        else:
            return 0

    '''
        Gets the valid moves of the piece
    '''
    def validMoves(self, rows, cols, turn):
        moves = list()
        piece = self.getPiece(rows, cols, turn)

        tempMoves = piece.validMove()
        for x in tempMoves:
            # This is for pieces with moves based on other pieces (bishop, rook, lance)
            # Checks if the valid move has +/- in any of the values
            if x[0] in {'+','-'} or x[1] in {'+','-'}:
                temp = [0,0]
                for dir in range(0,2):
                    if x[dir] == '+':
                        temp[dir] = 1
                    if x[dir] == '-':
                        temp[dir] = -1
                if piece.color == 1:
                    temp[1] *= -1

            # validSpot used for the while loop
            # count used to determine how many spaces in the temp direction the piece will move in
                validSquare = True
                count = 1
                while (validSquare):
                    # Checks if the said move relative to the current piece will be valid on the board
                    # rows/cols + (temp[] * count) = current square + (direction * magnitude)
                    if rows+(temp[0]*count) >= 0 and rows+(temp[0]*count) < 9 and cols+(temp[1]*count) >= 0 and cols+(temp[1]*count) < 9:
                        # If the valid move is not occupied, then change the validMove attribute of the square to be true
                        if not self.board[rows + (temp[0]*count)][cols + (temp[1]*count)].isOccupied:
                            self.board[rows + (temp[0]*count)][cols + (temp[1]*count)].validMove = True
                            moves.append([rows + (temp[0]*count), cols + (temp[1]*count)])
                            count += 1
                        # If the valid move is occupied
                        else:
                            validSquare = False
                            # If the occupied piece is of the opposite color, display the red square on that piece and then continue to the next operation
                            if turn%2 == 0:
                                for i in self.black.boardPieces:
                                    if i.square == self.board[rows + (temp[0]*count)][cols + (temp[1]*count)]:
                                        self.board[rows + (temp[0]*count)][cols + (temp[1]*count)].validMove = True
                                        moves.append([rows + (temp[0]*count), cols + (temp[1]*count)])
                                        validSquare = False
                                        pass
                            if turn%2 == 1:
                                for i in self.white.boardPieces:
                                    if i.square == self.board[rows + (temp[0]*count)][cols + (temp[1]*count)]:
                                        self.board[rows + (temp[0]*count)][cols + (temp[1]*count)].validMove = True
                                        moves.append([rows + (temp[0]*count), cols + (temp[1]*count)])
                                        validSquare = False
                                        pass
                            # If the occupied piece is of the same color, then continue to the next operation
                                else:
                                    validSquare = False
                    # If the move will be invalid, do not display and continue to next operation
                    else:
                        validSquare = False
            
            else:
                if rows+x[0] >= 0 and rows+x[0] < 9 and cols+x[1] >= 0 and cols+x[1] < 9:
                    if not self.board[rows + x[0]][cols + x[1]].isOccupied:
                        self.board[rows + x[0]][cols + x[1]].validMove = True
                        moves.append([rows + x[0], cols + x[1]])
                    else:
                        if turn%2 == 0:
                            for i in self.black.boardPieces:
                                if i.square == self.board[rows + x[0]][cols + x[1]]:
                                    self.board[rows + x[0]][cols + x[1]].validMove = True
                                    moves.append([rows + x[0], cols + x[1]])
                                    pass
                        if turn%2 == 1:
                            for i in self.white.boardPieces:
                                if i.square == self.board[rows + x[0]][cols + x[1]]:
                                    self.board[rows + x[0]][cols + x[1]].validMove = True
                                    moves.append([rows + x[0], cols + x[1]])
                                    pass
        return moves

    '''
        Resets each piece's validMove attribute to false
    '''
    def resetValidMoves(self):
        for j in range(0,9):
            for i in range(0,9):
                self.board[i][j].validMove = False

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
                        if x.square == self.board[i][j]:
                            print("b" + str(x), end=" ")

                    # for each white piece, find the piece with the current square
                    for x in self.white.boardPieces:
                        if x.square == self.board[i][j]:
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
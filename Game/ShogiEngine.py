from Board import Board
from Global import *
import pygame as p

"""
This class creates the board and runs most of the functions to play shogi.
"""
class GameState():
    def __init__(self) -> None:
        self.board = Board()
        self.turn = 0
        self.moveLog = []

    def getBoard(self):
        return self.board

    def printBoard(self):
        for row in self.board:
            print(*row)

    def movePiece(self, rows, cols, piece):
        if self.board.movePiece(rows, cols, piece) != 0:
            self.board.resetValidMoves()
            self.turn += 1
        else:
            self.board.resetValidMoves()
        

    def getValidMoves(self, rows, cols):
        self.board.validMoves(rows, cols, self.turn)

    def draw(self, screen, rows, cols):
        screen.fill(p.Color("#e6bc5c"))
        if (rows >= 0 and cols >= 0):
            self.drawHighlighted(screen, rows, cols)
        self.drawValidMoves(screen)
        self.drawBoard(screen)
        self.drawImages(screen)

    def drawBoard(self, screen):
        for x in range(0,10):
            p.draw.line(screen, p.Color("Black"), (x*tileSize + widthOffset, 0 + heightOffset), (x*tileSize + widthOffset, height + heightOffset))
            p.draw.line(screen, p.Color("Black"), (0 + widthOffset, x*tileSize + heightOffset), (width + widthOffset, x*tileSize + heightOffset))

    def drawImages(self, screen):
        for x in self.board.white.boardPieces:
            screen.blit(images["w" + str(x)], p.Rect(x.x*tileSize + widthOffset, x.y*tileSize + heightOffset, tileSize, tileSize))
        for x in self.board.black.boardPieces:
            screen.blit(images["b" + str(x)], p.Rect(x.x*tileSize + widthOffset, x.y*tileSize + heightOffset, tileSize, tileSize))

    def drawHighlighted(self, screen, rows, cols):
        p.draw.rect(screen, p.Color("#74e872"), p.Rect(rows*tileSize + widthOffset, cols*tileSize + heightOffset, tileSize, tileSize))

    def drawValidMoves(self, screen):
        for j in range(0,9):
            for i in range(0,9):
                # if the current square is a valid move
                if self.board.board[i][j].validMove:
                    p.draw.rect(screen, p.Color("red"), p.Rect(i*tileSize +tileSize*.05 + widthOffset, j*tileSize+tileSize*.05 + heightOffset, tileSize*.9, tileSize*.9))
        return
        # step 1: what piece is it
        if self.board.board[rows][cols].isOccupied:
            # For White Pieces
            if self.turn % 2 == 0:
                for x in self.board.white.boardPieces:
                    if x.square == self.board.board[rows][cols]:
        # step 2: what valid moves does the piece have
                        for y in x.validMove():
        # step 3: show valid moves of said piece
                        # This is for pieces with moves based on other pieces (bishop, rook, lance)
                            # Checks if the valid move has +/- in any of the values
                            if y[0] in {'+','-'} or y[1] in {'+','-'}:
                                # creates a temporary array that will be used to determine the direction of the piece
                                temp = [0,0]
                                for dir in range(0,2):
                                    if y[dir] == '+':
                                        temp[dir] = 1
                                    if y[dir] == '-':
                                        temp[dir] = -1
                                # validSpot used for the while loop
                                # count used to determine how many spaces in the temp direction the piece will move in
                                validSpot = True
                                count = 1
                                while (validSpot):
                                    # Checks if the said move relative to the current piece will be valid on the board
                                    # rows/cols + (temp[] * count) = current square + (direction * magnitude)
                                    if rows+(temp[0]*count) >= 0 and rows+(temp[0]*count) < 9 and cols+(temp[1]*count) >= 0 and cols+(temp[1]*count) < 9:
                                        # If the valid move is not occupied, then display the red square and increment the counter
                                        if not self.board.board[rows + (temp[0]*count)][cols + (temp[1]*count)].isOccupied:
                                            p.draw.rect(screen, p.Color("red"), p.Rect((rows+(temp[0]*count))*tileSize +tileSize*.05 + widthOffset, (cols+(temp[1]*count))*tileSize+tileSize*.05 + heightOffset, tileSize*.9, tileSize*.9))
                                            count += 1
                                        # If the valid move is occupied
                                        else:
                                            # If the occupied piece is of the opposite color, display the red square on that piece and then continue to the next operation
                                            for z in self.board.black.boardPieces:
                                                if z.currentSquare == self.board.board[rows + (temp[0]*count)][cols + (temp[1]*count)]:
                                                    p.draw.rect(screen, p.Color("red"), p.Rect((rows+(temp[0]*count))*tileSize +tileSize*.05 + widthOffset, (cols+(temp[1]*count))*tileSize+tileSize*.05 + heightOffset, tileSize*.9, tileSize*.9))
                                                    validSpot = False
                                            # If the occupied piece is of the same color, then continue to the next operation
                                            else:
                                                validSpot = False
                                    # If the move will be invalid, do not display and continue to next operation
                                    else:
                                        validSpot = False
                        # This is for pices with set moves (pawn, knight, silver general, gold general, king)
                            else:
                                if rows+y[0] >= 0 and rows+y[0] < 9 and cols+y[1] >= 0 and cols+y[1] < 9:
        # step 4: show valid moves only on spots where pieces dont occupy
                                    if not self.board.board[rows + y[0]][cols + y[1]].isOccupied:
                                        p.draw.rect(screen, p.Color("red"), p.Rect((rows+y[0])*tileSize +tileSize*.05 + widthOffset, (cols+y[1])*tileSize+tileSize*.05 + heightOffset, tileSize*.9, tileSize*.9))
                                    else:
                                        for z in self.board.black.boardPieces:
                                            if z.currentSquare == self.board.board[rows + y[0]][cols + y[1]]:
                                                p.draw.rect(screen, p.Color("red"), p.Rect((rows+y[0])*tileSize +tileSize*.05 + widthOffset, (cols+y[1])*tileSize+tileSize*.05 + heightOffset, tileSize*.9, tileSize*.9))
        # step 5: show valid moves only on spots where the piece can move                                   
            
            # For Black Pieces
            else:
                for x in self.board.black.boardPieces:
                    if x.currentSquare == self.board.board[rows][cols]:
                        for y in x.validMove():
        # step 3: show valid moves of said piece
                            # this is for pieces with moves based on other pieces (bishop, rook, lance)
                            if y[0] in {'+','-'} or y[1] in {'+','-'}:
                                temp = [0,0]
                                for dir in range(0,2):
                                    if y[dir] == '+':
                                        temp[dir] = 1
                                    if y[dir] == '-':
                                        temp[dir] = -1
                                validSpot = True
                                count = 1
                                while (validSpot):
                                    if rows+(temp[0]*count) >= 0 and rows+(temp[0]*count) < 9 and cols-(temp[1]*count) >= 0 and cols-(temp[1]*count) < 9:
                                        if not self.board.board[rows + (temp[0]*count)][cols - (temp[1]*count)].isOccupied:
                                            p.draw.rect(screen, p.Color("red"), p.Rect((rows+(temp[0]*count))*tileSize +tileSize*.05 + widthOffset, (cols-(temp[1]*count))*tileSize+tileSize*.05 + heightOffset, tileSize*.9, tileSize*.9))
                                            count += 1
                                        else:
                                            for z in self.board.white.boardPieces:
                                                if z.currentSquare == self.board.board[rows + (temp[0]*count)][cols - (temp[1]*count)]:
                                                    p.draw.rect(screen, p.Color("red"), p.Rect((rows+(temp[0]*count))*tileSize +tileSize*.05 + widthOffset, (cols-(temp[1]*count))*tileSize+tileSize*.05 + heightOffset, tileSize*.9, tileSize*.9))
                                                    validSpot = False
                                            else:
                                                validSpot = False
                                    else:
                                        validSpot = False
                            # this is for pices with set moves (pawn, knight, silver general, gold general, king)
                            else:
                                if rows+y[0] >= 0 and rows+y[0] < 9 and cols-y[1] >= 0 and cols-y[1] < 9:
                                    if not self.board.board[rows + y[0]][cols - y[1]].isOccupied:
        # step 4: show valid moves only on spots where pieces dont occupy
                                        p.draw.rect(screen, p.Color("red"), p.Rect((rows+y[0])*tileSize +tileSize*.05 + widthOffset, (cols-y[1])*tileSize+tileSize*.05 + heightOffset, tileSize*.9, tileSize*.9))
        # step 5: show valid moves only on spots where the piece's valid moves are not of the same color
                                    else:
                                        for z in self.board.white.boardPieces:
                                            if z.currentSquare == self.board.board[rows + y[0]][cols - y[1]]:
                                                p.draw.rect(screen, p.Color("red"), p.Rect((rows+y[0])*tileSize +tileSize*.05 + widthOffset, (cols-y[1])*tileSize+tileSize*.05 + heightOffset, tileSize*.9, tileSize*.9))

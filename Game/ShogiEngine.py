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

    # Currently only increases the turn count
    def movePiece(self):
        self.board.movePiece() # does nothing at the moment
        self.turn += 1


    def draw(self, screen, rows, cols):
        screen.fill(p.Color("#e6bc5c"))
        if (rows >= 0 and cols >= 0):
            self.drawHighlighted(screen, rows, cols)
            self.drawValidMoves(screen, rows, cols)
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

    def drawValidMoves(self, screen, rows, cols):
        # step 1: what piece is it
        if self.board.board[rows][cols].isOccupied:
            if self.turn % 2 == 0:
                for x in self.board.white.boardPieces:
                    if x.currentSquare == self.board.board[rows][cols]:
        # step 2: what valid moves does the piece have
                        for y in x.validMove():
        # step 3: show valid moves of said piece
                            if rows+y[0] >= 0 and rows+y[0] < 9 and cols+y[1] >= 0 and cols+y[1] < 9:
                                if not self.board.board[rows + y[0]][cols + y[1]].isOccupied:
                                    p.draw.rect(screen, p.Color("red"), p.Rect((rows+y[0])*tileSize +tileSize*.05 + widthOffset, (cols+y[1])*tileSize+tileSize*.05 + heightOffset, tileSize*.9, tileSize*.9))
            else:
                for x in self.board.black.boardPieces:
                    if x.currentSquare == self.board.board[rows][cols]:
                        for y in x.validMove():
                            if rows+y[0] >= 0 and rows+y[0] < 9 and cols-y[1] >= 0 and cols-y[1] < 9:
                                if not self.board.board[rows + y[0]][cols + y[1]].isOccupied:
                                    p.draw.rect(screen, p.Color("red"), p.Rect((rows+y[0])*tileSize +tileSize*.05 + widthOffset, (cols-y[1])*tileSize+tileSize*.05 + heightOffset, tileSize*.9, tileSize*.9))
        # step 4: show valid moves only on spots where pieces dont occupy
        # step 5: show valid moves only on spots where the piece's valid moves are not of the same color
        else:
            pass
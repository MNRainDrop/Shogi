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

    def draw(self, screen, rows, cols):
        screen.fill(p.Color("#e6bc5c"))
        self.drawHighlighted(screen, rows, cols)
        self.drawValidMoves(screen, rows, cols)
        self.drawBoard(screen)
        self.drawImages(screen)

    # Currently only increases the turn count
    def movePiece(self):
        self.board.movePiece() # does nothing at the moment
        self.turn += 1

    def drawBoard(self, screen):
        for x in range(1,9):
            p.draw.line(screen, p.Color("Black"), (x*tileSize, 0), (x*tileSize, height))
            p.draw.line(screen, p.Color("Black"), (0, x*tileSize), (width, x*tileSize))

    def drawImages(self, screen):
        for x in self.board.white.boardPieces:
            screen.blit(images["w" + str(x)], p.Rect(x.x*tileSize, x.y*tileSize, tileSize, tileSize))
        for x in self.board.black.boardPieces:
            screen.blit(images["b" + str(x)], p.Rect(x.x*tileSize, x.y*tileSize, tileSize, tileSize))

    def drawHighlighted(self, screen, rows, cols):
        p.draw.rect(screen, p.Color("#74e872"), p.Rect(rows*tileSize, cols*tileSize, tileSize, tileSize))

    def drawValidMoves(self, screen, rows, cols):
        # step 1: what piece is it
        if self.board.board[cols][rows].isOccupied:
            if self.turn % 2 == 0:
                for x in self.board.white.boardPieces:
                    if x.currentSquare == self.board.board[cols][rows]:
        # step 2: what valid moves does the piece have
                        for y in x.validMove():
        # step 3: show valid moves of said piece
                            p.draw.rect(screen, p.Color("red"), p.Rect((rows+y[0])*tileSize +tileSize*.05, (cols+y[1])*tileSize+tileSize*.05, tileSize*.9, tileSize*.9))
            else:
                for x in self.board.black.boardPieces:
                    if x.currentSquare == self.board.board[cols][rows]:
                        for y in x.validMove():
                            p.draw.rect(screen, p.Color("red"), p.Rect((rows+y[0])*tileSize +tileSize*.05, (cols-y[1])*tileSize+tileSize*.05, tileSize*.9, tileSize*.9))
        # step 4: show valid moves only on spots where pieces dont occupy
        # step 5: show valid moves only on spots where the piece's valid moves are not of the same color
        else:
            pass
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
        self.drawBoard(screen)
        self.drawImages(screen)

    def drawBoard(self, screen):
        for x in range(1,9):
            p.draw.line(screen, p.Color("Black"), (x*tileSize, 0), (x*tileSize, height))
            p.draw.line(screen, p.Color("Black"), (0, x*tileSize), (width, x*tileSize))

    def drawImages(self, screen):
        for x in self.board.white.boardPieces:
            screen.blit(images["w" + str(x)], p.Rect(x.x*tileSize, x.y*tileSize, tileSize, tileSize))
        for x in self.board.black.boardPieces:
            screen.blit(images["b" + str(x)], p.Rect(x.x*tileSize, x.y*tileSize, tileSize, tileSize))

    def drawHighlighted(self, screen, cols, rows):
        p.draw.rect(screen, p.Color("#74e872"), p.Rect(rows*tileSize, cols*tileSize, tileSize, tileSize))
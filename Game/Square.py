from Piece import *
"""
This class handles each Square on the board.

Every Square belongs on a Board.
Every Square can have zero to one pieces.
"""

class Square():
    def __init__(self, x, y, isOccupied = False) -> None:
        self.x = x
        self.y = y
        self.isOccupied = isOccupied
        self.occupiedBy = None

    def setOccupiedBy(self, piece):
        self.isOccupied = True
        self.occupiedBy = piece

    def __str__(self) -> str:
        if self.isOccupied == False:
            return "---"
        else:
            return self.occupiedBy.__str__()
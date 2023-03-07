from Piece import *

"""
This handles all actions taken with the Player.

Every player has zero to many Pieces at once time.
"""
class Player():
    def __init__(self) -> None:
        self.boardPieces = list()
        self.sidePieces = list()
        
    def takePiece(self):
        pass
    
    def dropPiece(self):
        pass
"""
This class creates an Abstract class for Pieces.
The children of Pieces handle the valid moves.
"""
class Piece():
    def __init__(self, rank: str, isPromoted, playerNum) -> None:
        self.rank = rank
        self.isPromoted = isPromoted
        self.playerNum = playerNum

    def validMove(self):
        pass

    def __str__(self) -> str:
        if self.isPromoted:
            return str(self.playerNum + "p" + self.rank)
        else:
            return str(self.playerNum + " " + self.rank)

class Pawn(Piece):
    def __init__(self, playerNum) -> None:
        super().__init__("p", False, playerNum)

    def validMove(self):
        pass

class Bishop(Piece):
    def validMove(self):
        pass

class Rook():
    def validMove():
        pass

class Rook():
    def validMove():
        pass

class Lance():
    def validMove():
        pass

class Knight():
    def validMove():
        pass

class SilverGeneral():
    def validMove():
        pass

class GoldGeneral():
    def validMove():
        pass

class King():
    def validMove():
        pass
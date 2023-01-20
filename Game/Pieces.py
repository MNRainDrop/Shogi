"""
This class creates an Abstract class for Pieces.
The children of Pieces handle the valid moves.
"""
class Piece():
    def __init__(self, side, x, y) -> None:
        self.side = side
        self.x = x
        self.y = y

    def validMove():
        pass

class Pawn(Piece):
    def validMove(self, board):
        isValid = {}
        if self.side == "w":
            if board[self.x][self.y-1] == "   ":
                isValid.append((self.x, self.y-1))
        if self.side == "b":
            if board[self.x][self.y+1] == "   ":
                isValid.append((self.x, self.y+1))

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
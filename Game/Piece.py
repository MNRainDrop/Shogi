from Square import Square
"""
This class creates an Abstract class for Pieces.
The children of Pieces handle the valid moves.
"""
class Piece():
    def __init__(self, rank: str, isPromoted, square : Square) -> None:
        self.rank = rank
        self.isPromoted = isPromoted
        self.currentSquare = square
        self.x = self.currentSquare.x
        self.y = self.currentSquare.y

    def validMove(self) -> list:
        # the valid moves list will append each possible move per piece using a tuple
        # format for the tuple will be (x, y)
        # y = up - / down +
        # x = left - / right +
        pass

    def __str__(self) -> str:
        if self.isPromoted:
            return str("p" + self.rank)
        else:
            return str(" " + self.rank)

class Pawn(Piece):
    def __init__(self, square) -> None:
        super().__init__("P", False, square)

    def validMove(self) -> list:
        validMoves = list()
        validMoves.append((0,-1))
        return validMoves

class Bishop(Piece):
    def __init__(self, square) -> None:
        super().__init__("B", False, square)

    def validMove(self, x, y) -> list:
        pass

class Rook(Piece):
    def __init__(self, square) -> None:
        super().__init__("R", False, square)

    def validMove(self, x, y) -> list:
        pass

class Lance(Piece):
    def validMove(self, x, y) -> list:
        pass

class Knight(Piece):
    def validMove(self, x, y) -> list:
        pass

class SilverGeneral(Piece):
    def validMove(self, x, y) -> list:
        pass

class GoldGeneral(Piece):
    def validMove(self, x, y) -> list:
        pass

class King(Piece):
    def __init__(self, square) -> None:
        super().__init__("K", False, square)

    def validMove(self) -> list:
        validMoves = list()
        validMoves.append(1,0)
        validMoves.append(0,1)
        validMoves.append(-1,0)
        validMoves.append(0,-1)
        validMoves.append(1,1)
        validMoves.append(1,-1)
        validMoves.append(-1,1)
        validMoves.append(-1,-1)
        return validMoves
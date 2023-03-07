from Square import Square

'''
This class creates an Abstract class for Pieces.
The children of Pieces handle the valid moves.
'''
class Piece():
    def __init__(self, rank: str, isPromoted, square : Square) -> None:
        self.rank = rank
        self.isPromoted = isPromoted
        self.square = square
        self.x = self.square.x
        self.y = self.square.y
        self.color = 0

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
        validMoves.append([0,-1])
        if self.color == 1:
            for i in validMoves:
                i[1] *= -1
        return validMoves

class Bishop(Piece):
    def __init__(self, square) -> None:
        super().__init__("B", False, square)

    def validMove(self) -> list:
        validMoves = list()
        validMoves.append(['+','+'])
        validMoves.append(['+','-'])
        validMoves.append(['-','+'])
        validMoves.append(['-','-'])
        return validMoves

class Rook(Piece):
    def __init__(self, square) -> None:
        super().__init__("R", False, square)

    def validMove(self) -> list:
        validMoves = list()
        validMoves.append(['+',0])
        validMoves.append([0,'+'])
        validMoves.append(['-',0])
        validMoves.append([0,'-'])
        return validMoves

class Lance(Piece):
    def __init__(self, square) -> None:
        super().__init__("L", False, square)

    def validMove(self) -> list:
        validMoves = list()
        validMoves.append([0,'-'])
        return validMoves

class Knight(Piece):
    def __init__(self, square) -> None:
        super().__init__("N", False, square)

    def validMove(self) -> list:
        validMoves = list()
        validMoves.append([-1,-2])
        validMoves.append([1,-2])
        validMoves.append([-1,2])
        validMoves.append([1,2])
        validMoves.append([2,1])
        validMoves.append([2,-1])
        validMoves.append([-2,1])
        validMoves.append([-2,-1])
        if self.color == 1:
            for i in validMoves:
                i[1] *= -1
        return validMoves

class SilverGeneral(Piece):
    def __init__(self, square) -> None:
        super().__init__("S", False, square)

    def validMove(self) -> list:
        validMoves = list()
        validMoves.append([-1,-1])
        validMoves.append([1,-1])
        validMoves.append([0,-1])
        validMoves.append([-1,1])
        validMoves.append([1,1])
        if self.color == 1:
            for i in validMoves:
                i[1] *= -1
        return validMoves

class GoldGeneral(Piece):
    def __init__(self, square) -> None:
        super().__init__("G", False, square)

    def validMove(self) -> list:
        validMoves = list()
        validMoves.append([1,0])
        validMoves.append([-1,0])
        validMoves.append([0,-1])
        validMoves.append([0,1])
        validMoves.append([-1,-1])
        validMoves.append([1,-1])
        if self.color == 1:
            for i in validMoves:
                i[1] *= -1
        return validMoves

class King(Piece):
    def __init__(self, square) -> None:
        super().__init__("K", False, square)

    def validMove(self) -> list:
        validMoves = list()
        validMoves.append([0,1])
        validMoves.append([0,-1])
        validMoves.append([1,0])
        validMoves.append([-1,0])
        validMoves.append([1,1])
        validMoves.append([1,-1])
        validMoves.append([-1,1])
        validMoves.append([-1,-1])
        if self.color == 1:
            for i in validMoves:
                i[1] *= -1
        return validMoves
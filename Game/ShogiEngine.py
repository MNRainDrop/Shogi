"""
This class creats the board and runs most of the functions to play shogi.
"""
class GameState():
    def __init__(self) -> None:
        self.board = [
            ["b L", "b N", "b S", "b G", "b K", "b G", "b S", "b N", "b L"],
            ["   ", "b B", "   ", "   ", "   ", "   ", "   ", "b R", "   "],
            ["b P", "b P", "b P", "b P", "b P", "b P", "b P", "b P", "b P"],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["w P", "w P", "w P", "w P", "w P", "w P", "w P", "w P", "w P"],
            ["   ", "w B", "   ", "   ", "   ", "   ", "   ", "w R", "   "],
            ["w L", "w N", "w S", "w G", "w K", "w G", "w S", "w N", "w L"]
        ]
        self.turn = 0
        self.moveLog = []

    def getBoard(self):
        return self.board

    def printBoard(self):
        for row in self.board:
            print(*row)
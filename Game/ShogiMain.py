import pygame as p
import ShogiEngine

height = width = 900
boardSize = 9
tileSize = height / boardSize
maxFPS = 15
images = []



# Main Game Driver
def main():

    #initialize pygame
    p.init()
    screen = p.display.set_mode((height, width))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    #initalize ShogiEngine game state in the gs (game state) variable
    gs = ShogiEngine.GameState()
    gs.printBoard()

if __name__ == "__main__":
    main()
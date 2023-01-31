import pygame as p
from Global import *
from ShogiEngine import GameState

# Main Game Driver
def main():

    #initialize pygame
    p.init()
    screen = p.display.set_mode((height, width))
    clock = p.time.Clock()

    #initialize images
    loadImages()

    #initalize ShogiEngine game state in the gs (game state) variable
    gs = GameState()
    running = True

    

    rows = -1
    cols = -1

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if e.button == 3:
                    location = p.mouse.get_pos() 
                    cols = location[1] // tileSize
                    rows = location[0] // tileSize

            # Incrememnts the turn count so we can test the valid moves
            elif e.type == p.KEYDOWN:
                if e.key == p.K_1:
                    gs.movePiece()

        #draws everything
        gs.draw(screen, rows, cols)
        
        p.display.update()
        
        clock.tick(maxFPS)
        p.display.flip()


def loadImages():
    pieces = ["b L", "b N", "b S", "b G", "b K", "b B", "b R", "b P", "w L", "w N", "w S", "w G", "w K", "w B", "w R", "w P"]
    #promotedPieces = ["bPL", "bPN", "bPS", "bPB", "bPR", "bPP", "wPL", "wPN", "wPS", "wPB", "wPR", "wPP"]
                
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("Game/images/" + piece + ".png"), (tileSize, tileSize))




if __name__ == "__main__":
    main()
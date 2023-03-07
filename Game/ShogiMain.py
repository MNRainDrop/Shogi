import pygame as p
from Global import *
from ShogiEngine import GameState

# Main Game Driver
def main():

    #initialize pygame
    p.init()
    screen = p.display.set_mode((width + 400, height + 100))
    clock = p.time.Clock()

    #initialize images
    loadImages()

    #initalize ShogiEngine game state in the gs (game state) variable
    gs = GameState()
    running = True

    

    rows = -1
    cols = -1
    validClick = 1

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if e.button == 1:
                    #on left mouse click down
                    #select piece and show valid moves
                    #will be used to drag pieces
                    location = p.mouse.get_pos() 
                    cols = (location[1] - heightOffset) // tileSize
                    rows = (location[0] - widthOffset) // tileSize
                    if cols >= 9 or cols < 0:
                        cols = -1
                    if rows >= 9 or rows < 0:
                        rows = -1
                    try:
                        piece = gs.board.getPiece(rows, cols, gs.turn)
                        gs.getValidMoves(rows, cols)
                    except:
                        validClick = 0
                        piece = None
                    else:
                        validClick = 1
            elif e.type == p.MOUSEBUTTONUP and validClick:
                if e.button == 1:
                    #on left click up
                    #selected piece will be placed in certain spot
                    location = p.mouse.get_pos() 
                    cols = (location[1] - heightOffset) // tileSize
                    rows = (location[0] - widthOffset) // tileSize
                    if cols >= 9 or cols < 0:
                        cols = -1
                    if rows >= 9 or rows < 0:
                        rows = -1
                    gs.movePiece(rows, cols, piece)
                    validClick = 0

            # Incrememnts the turn count so we can test the valid moves
            elif e.type == p.KEYDOWN:
                if e.key == p.K_1:
                    gs.movePiece(rows, cols)

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
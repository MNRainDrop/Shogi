import pygame as p
import ShogiEngine


tileSize = 80
boardSize = 9
height = width = boardSize*tileSize
maxFPS = 15
images = {}



# Main Game Driver
def main():

    #initialize pygame
    p.init()
    screen = p.display.set_mode((height, width))
    clock = p.time.Clock()
    screen.fill(p.Color("#e6bc5c"))

    #initialize images
    loadImages()

    #initalize ShogiEngine game state in the gs (game state) variable
    gs = ShogiEngine.GameState()
    running = True

    #draws the lines on the board
    drawBoard(screen)
    #draws the pieces onto the board
    drawImages(screen, gs.board)



    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        clock.tick(maxFPS)
        p.display.flip()

def loadImages():
    pieces = ["b L", "b N", "b S", "b G", "b K", "b B", "b R", "b P", "w L", "w N", "w S", "w G", "w K", "w B", "w R", "w P"]
    #promotedPieces = ["bPL", "bPN", "bPS", "bPB", "bPR", "bPP", "wPL", "wPN", "wPS", "wPB", "wPR", "wPP"]
                
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("Pieces/" + piece + ".png"), (tileSize, tileSize))

        
def drawBoard(screen,):
    for x in range(1,9):
        p.draw.line(screen, p.Color("Black"), (x*tileSize, 0), (x*tileSize, height))
        p.draw.line(screen, p.Color("Black"), (0, x*tileSize), (width, x*tileSize))

def drawImages(screen, board):
    for rows in range(boardSize):
        for cols in range(boardSize):
            piece = board[rows][cols]
            if piece != "   ":
                screen.blit(images[piece], p.Rect(cols*tileSize, rows*tileSize, tileSize, tileSize))


if __name__ == "__main__":
    main()
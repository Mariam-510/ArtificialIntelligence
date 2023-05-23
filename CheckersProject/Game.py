import pygame
from Board import Board

# Player
Black = (33, 33, 33)
Beige = (255, 209, 122)


class Game:
    def __init__(self, gameWindow):
        self.board = Board()
        self.gameWindow = gameWindow

    def generateNewBoard(self):
        self.board.makeGui(self.gameWindow)
        pygame.display.update()

    def setBoard(self, board):
        self.board = board
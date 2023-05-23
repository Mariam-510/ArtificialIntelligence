import pygame
import random
import time
from Game import Game
from MiniMax import minimax
from AlphaBeta import alphaBeta

# Player
Black = (33, 33, 33)
Beige = (255, 209, 122)
# No Winner
White = (255, 255, 255)


def start(algo, level):
    play = True
    gameWindow = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Checkers')
    game = Game(gameWindow)
    game.turn = Beige
    depth = 0
    if level == 1:  # easy
        depth = 2
    if level == 2:  # medium
        depth = 3
    if level == 3:  # hard
        depth = 4

    while play:
        if game.turn == Black:
            if algo == 1:
                list = minimax(game.board, Black, depth)
            elif algo == 2:
                list = alphaBeta(game.board, Black, depth, float('-inf'), float('inf'))
            game.setBoard(list[0])
            game.turn = Beige

        elif game.turn == Beige:
            players = game.board.getPlayersVaildMoves(Beige)
            if len(players) == 0:
                game.board.remainBeige = 0
            else:
                maxLenPlayerSkip = -1  # > skip player
                maxLenPlayerSkipIndex = -1  # > index skip
                maxLenPlayerIndex = -1
                c = 0
                for p in players:  # loop player
                    playerMoves = game.board.NextMoves(p)  # { {(1,2)[0,2][2,2]} {} {}}
                    i = 0
                    maxLen = -1
                    maxIndex = -1
                    for move, skip in playerMoves.items():  # {m ,s}
                        if len(skip) > maxLen:
                            maxLen = len(skip)
                            maxIndex = i
                        i += 1
                    if maxLen > maxLenPlayerSkip:
                        maxLenPlayerIndex = c
                        maxLenPlayerSkip = maxLen
                        maxLenPlayerSkipIndex = maxIndex
                    c += 1

                if maxLenPlayerSkip == 0:
                    maxLenPlayerIndex = random.randint(0, len(players) - 1)
                    maxLenPlayerSkipIndex = random.randint(0, len(players) - 1)
                playerMoves = game.board.NextMoves(players[maxLenPlayerIndex])
                i = 0
                for move, skip in playerMoves.items():
                    if i == maxLenPlayerSkipIndex:
                        break
                    else:
                        i += 1

                game.board.movePlayerAndRmoveOpponentList(players[maxLenPlayerIndex], move[0], move[1], skip)
            game.turn = Black

        if game.board.ckeckWinner() != White:
            if game.board.ckeckWinner() == Beige:
                print('Beige is winner :)')
            elif game.board.ckeckWinner() == Black:
                print('Black is winner :)')
            play = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

        game.generateNewBoard()
        time.sleep(1)

    pygame.quit()
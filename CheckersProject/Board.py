import pygame
from Player import Player

# Player
Black = (33, 33, 33)
Beige = (255, 209, 122)
# Background
Brown = (93, 64, 55)
LightBeige = (255, 224, 178)
# No Winner
White = (255, 255, 255)


class Board:
    def __init__(self):
        self.remainBeige = self.remainBlack = 12
        self.beigeKings = self.blackKings = 0
        self.board = []
        self.initializeEmptyBoard()
        self.addBlackPlayerToBoard()
        self.addBeigePlayerToBoard()

    def initializeEmptyBoard(self):
        self.board = [[0] * 8 for _ in range(8)]

    def addBlackPlayerToBoard(self):
        for row in range(3):
            for col in range(8):
                if (col + row) % 2 == 1:
                    self.board[row][col] = Player(row, col, Black)

    def addBeigePlayerToBoard(self):
        for row in range(5, 8):
            for col in range(8):
                if (col + row) % 2 == 1:
                    self.board[row][col] = Player(row, col, Beige)

    # make Gui
    def makeGui(self, display):
        # make Gui Board
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(display, LightBeige, (row * 100, col * 100, 100, 100))
                else:
                    pygame.draw.rect(display, Brown, (row * 100, col * 100, 100, 100))

        # make Gui Player
        for row in range(8):
            for col in range(8):
                player = self.board[row][col]
                if player != 0:
                    pygame.draw.circle(display, player.color, (player.x_Gui, player.y_Gui), 40)
                    if player.king:
                        display.blit(pygame.image.load('Crown.png'), (player.x_Gui - 22, player.y_Gui - 22))


    def checkerHeuristicFunction(self):
        return (self.remainBlack + self.blackKings) - (self.remainBeige + self.beigeKings)

    def getPlayers(self, c):
        players = []
        for r in self.board:
            for player in r:
                if player != 0:
                    if player.color == c:
                        players.append(player)
        return players

    def getPlayersVaildMoves(self, c):
        players = []
        for r in self.board:
            for player in r:
                if player != 0:
                    if player.color == c and self.NextMoves(player):
                        players.append(player)
        return players

    def getPlayer(self, r, c):
        return self.board[r][c]

    def movePlayerAndRmoveOpponentList(self, player, r, c, opponentList):
        self.board[player.row][player.col] = 0
        player.row = r
        player.col = c
        player.x_Gui = 100 * c + 50
        player.y_Gui = 100 * r + 50
        self.board[r][c] = player

        if r == 7 and not player.king:
            player.king = True
            self.blackKings += 1
        if r == 0 and not player.king:
            player.king = True
            self.beigeKings += 1

        for opponent in opponentList:
            self.board[opponent.row][opponent.col] = 0
            if opponent.color == Beige:
                self.remainBeige -= 1
            elif opponent.color == Black:
                self.remainBlack -= 1

    def ckeckWinner(self):
        if self.remainBeige != 0 and self.remainBlack != 0:
            return White
        elif self.remainBeige == 0 and self.remainBlack != 0:
            return Black
        elif self.remainBlack == 0 and self.remainBeige != 0:
            return Beige


    def NextMoves(self, player):
        change1 = -1
        end1 = -1
        if (player.row - 3) > end1:
            end1 = player.row - 3

        change2 = 1
        end2 = 8
        if (player.row + 3) < end2:
            end2 = player.row + 3

        nextMoves = {}

        if player.king:
            nextMoves.update(self.check(player.row + change1, end1, change1, player.color, player.col - 1, False, []))
            nextMoves.update(self.check(player.row + change1, end1, change1, player.color, player.col + 1, True, []))
            nextMoves.update(self.check(player.row + change2, end2, change2, player.color, player.col - 1, False, []))
            nextMoves.update(self.check(player.row + change2, end2, change2, player.color, player.col + 1, True, []))

        elif player.color == Beige:
            nextMoves.update(self.check(player.row + change1, end1, change1, player.color, player.col - 1, False, []))
            nextMoves.update(self.check(player.row + change1, end1, change1, player.color, player.col + 1, True, []))

        elif player.color == Black:
            nextMoves.update(self.check(player.row + change2, end2, change2, player.color, player.col - 1, False, []))
            nextMoves.update(self.check(player.row + change2, end2, change2, player.color, player.col + 1, True, []))

        return nextMoves

    def check(self, begin, end, change, color, col, flag, eaten):
        recentEaten = []
        nextMoves = {}

        row = begin
        while row != end:
            if col > 7 or col < 0:
                break

            if self.board[row][col] != 0:
                if self.board[row][col].color == color:
                    break

                elif self.board[row][col].color != color:
                    recentEaten = [self.board[row][col]]

            else:
                if len(eaten) == 0:
                    nextMoves[(row, col)] = recentEaten
                else:
                    if len(recentEaten) == 0:
                        break
                    elif len(recentEaten) != 0:
                        nextMoves[(row, col)] = recentEaten + eaten

                if len(recentEaten) != 0:
                    if change == 1:
                        endRow = 8
                        if (row + 3) < endRow:
                            endRow = row + 3

                    elif change == -1:
                        endRow = 0
                        if (row - 3) > endRow:
                            endRow = row - 3

                    nextMoves.update(self.check(row + change, endRow, change, color, col - 1, False, recentEaten))
                    nextMoves.update(self.check(row + change, endRow, change, color, col + 1, True, recentEaten))

                break

            row += change

            if flag:
                col += 1
            else:
                col -= 1

        return nextMoves
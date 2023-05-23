from copy import deepcopy

# Player
Black = (33, 33, 33)
Beige = (255, 209, 122)
# No Winner
White = (255, 255, 255)

def minimax(currentBoard, color, level):
    if level != 0 and currentBoard.ckeckWinner() == White:

        if color == Beige:
            list = [None, float('inf')]

            nextStates = []
            for player in currentBoard.getPlayers(color):
                for nextState, opponentList in currentBoard.NextMoves(player).items():
                    possibleBoard = deepcopy(currentBoard)
                    possiblePlayer = possibleBoard.getPlayer(player.row, player.col)
                    possibleBoard.movePlayerAndRmoveOpponentList(possiblePlayer, nextState[0], nextState[1], opponentList)
                    nextStates.append(possibleBoard)

            for state in nextStates:
                tempList = minimax(state, Black, level - 1)
                if tempList[1] < list[1]:
                    list[1] = tempList[1]
                    list[0] = state

            return list

        elif color == Black:
            list = [None, float('-inf')]

            nextStates = []
            for player in currentBoard.getPlayers(color):
                for nextState, opponentList in currentBoard.NextMoves(player).items():
                    possibleBoard = deepcopy(currentBoard)
                    possiblePlayer = possibleBoard.getPlayer(player.row, player.col)
                    possibleBoard.movePlayerAndRmoveOpponentList(possiblePlayer, nextState[0], nextState[1], opponentList)
                    nextStates.append(possibleBoard)

            for state in nextStates:
                tempList = minimax(state, Beige, level - 1)
                if tempList[1] > list[1]:
                    list[1] = tempList[1]
                    list[0] = state

            return list

    else:
        list = [currentBoard, currentBoard.checkerHeuristicFunction()]
        return list
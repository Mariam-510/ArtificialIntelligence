class Player:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.x_Gui = 100 * self.col + 50
        self.y_Gui = 100 * self.row + 50
        self.color = color
        self.king = False
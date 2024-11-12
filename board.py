class Board:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        if self.board[row][col] == "":
            self.board[row][col] = player
            return True
        return False

    def check_winner(self):
        # Проверка строк, столбцов и диагоналей
        for line in self.board + list(zip(*self.board)):
            if len(set(line)) == 1 and line[0] != "":
                return line[0]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        return None

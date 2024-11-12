from player import Player
from board import Board

class Game:
    def init(self):
        self.player = Player()
        self.board = Board()
        self.winner = None

    def play_turn(self, row, col):
        if self.winner is None and self.board.make_move(row, col, self.player.get_player()):
            self.winner = self.board.check_winner()
            if self.winner is None:
                self.player.switch_player()
            return True
        return False

    def get_winner(self):
        return self.winner

    def reset_game(self):
        self.board.reset_board()
        self.winner = None
        self.player = Player()
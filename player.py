class Player:
    def init(self):
        self.current_player = "X"

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def get_player(self):
        return self.current_player
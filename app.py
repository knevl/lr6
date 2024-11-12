import tkinter as tk
from game import Game

class App:
    def __init__(self, root):
        self.root = root
        self.game = Game()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def handle_click(self, row, col):
        if self.game.play_turn(row, col):
            self.buttons[row][col].config(text=self.game.player.get_player())
            winner = self.game.get_winner()
            if winner:
                self.show_winner(winner)

    def show_winner(self, winner):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")
        self.reset_button.config(text=f"{winner} Wins! Play Again?")

    def reset_game(self):
        self.game.reset_game()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state="normal")
        self.reset_button.config(text="Reset")

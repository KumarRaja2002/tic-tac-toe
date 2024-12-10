import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # Player is "X"
        self.ai_player = "O"      # AI is "O"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        self.window.mainloop()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.window, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def handle_click(self, row, col):
        if self.board[row][col] == "" and self.current_player == "X":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", "You win!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = self.ai_player
                self.ai_move()

    def ai_move(self):
        move = self.best_move()
        row, col = move
        self.board[row][col] = self.ai_player
        self.buttons[row][col].config(text=self.ai_player)

        if self.check_winner(self.ai_player):
            messagebox.showinfo("Game Over", "AI wins!")
            self.reset_board()
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_board()
        else:
            self.current_player = "X"

    def best_move(self):
        # AI strategy: Try to win, block player, or take random move
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    self.board[row][col] = self.ai_player
                    if self.check_winner(self.ai_player):
                        return (row, col)
                    self.board[row][col] = ""  # Undo move

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    self.board[row][col] = "X"
                    if self.check_winner("X"):
                        self.board[row][col] = ""  # Undo move
                        return (row, col)
                    self.board[row][col] = ""  # Undo move

        # Take random available position
        empty_cells = [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == ""]
        return random.choice(empty_cells)

    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != "" for row in self.board for cell in row)

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ""
                self.buttons[row][col].config(text="")
        self.current_player = "X"  # Player starts the new game


if __name__ == "__main__":
    TicTacToe()

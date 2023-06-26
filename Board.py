from tkinter import *


class Board:
    def __init__(self, size=15):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]

    def move(self, x, y, player):
        if self.board[x][y] == '.':
            self.board[x][y] = player.symbol
            return True
        return False

    def check_game_over(self, x, y, player):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 0
            for i in range(-4, 5):
                nx, ny = x + dx * i, y + dy * i
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player.symbol:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
        return False

    def check_game_over_with_assumed_move_new(self, x, y, player_symbol) -> int:
        score = 0
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                nx, ny = x + dx * i, y + dy * i
                if i == 1 and 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] != '.':
                    player_symbol = self.board[nx][ny]
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player_symbol:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                nx, ny = x - dx * i, y - dy * i
                if i == 1 and 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] != '.':
                    player_symbol = self.board[nx][ny]
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player_symbol:
                    count += 1
                else:
                    break
            if player_symbol == "X":
                if count >= 4:
                    score += 8000
                elif count == 3:
                    score += 200
                elif count == 2:
                    score += 10
                elif count == 1:
                    score += 1
            else:
                if count >= 4:
                    score += 7500
                elif count == 3:
                    score += 180
                elif count == 2:
                    score += 12
                elif count == 1:
                    score += 2
        return score

    def check_game_over_with_assumed_move_medium1(self, x, y, player_symbol) -> int:
        score = 0
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                nx, ny = x + dx * i, y + dy * i
                if i == 1 and 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] != '.':
                    player_symbol = self.board[nx][ny]
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player_symbol:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                nx, ny = x - dx * i, y - dy * i
                if i == 1 and 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] != '.':
                    player_symbol = self.board[nx][ny]
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player_symbol:
                    count += 1
                else:
                    break
            if player_symbol == "X":
                if count >= 4:
                    score += 800
                elif count == 3:
                    score += 150
                elif count == 2:
                    score += 10
                elif count == 1:
                    score += 1
            else:
                if count >= 4:
                    score += 750
                elif count == 3:
                    score += 130
                elif count == 2:
                    score += 12
                elif count == 1:
                    score += 2
        return score

    def check_game_over_with_assumed_move_easy(self, x, y, player_symbol) -> int:
        score = 0
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                nx, ny = x + dx * i, y + dy * i
                if i == 1 and 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] != '.':
                    player_symbol = self.board[nx][ny]
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player_symbol:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                nx, ny = x - dx * i, y - dy * i
                if i == 1 and 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] != '.':
                    player_symbol = self.board[nx][ny]
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player_symbol:
                    count += 1
                else:
                    break
            if count >= 4:
                score += 100
            elif count == 3:
                score += 50
            elif count == 2:
                score += 8
            elif count == 1:
                score += 1
        return score

    def check_game_over_with_assumed_move(self, x, y, player_symbol):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                nx, ny = x + dx * i, y + dy * i
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player_symbol:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                nx, ny = x - dx * i, y - dy * i
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player_symbol:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

    def display(self):
        for row in self.board:
            print(' '.join(row))

    def get_empty_positions(self):
        return [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == '.']




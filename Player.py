import random
import Board
import numpy as np


class Player:
    def __init__(self, symbol):
        self.symbol = symbol


class ComputerPlayer(Player):
    def __init__(self, symbol, difficulty):
        super().__init__(symbol)
        self.difficulty = difficulty

    def make_move(self, board):
        if self.difficulty == 'difficult':
            print('difficult_Computer is thinking...')
            best_score = -1
            best_move = []
            for i in range(board.size):
                for j in range(board.size):
                    if board.board[i][j] == '.':
                        score = self.evaluate_position_difficult(board, i, j)
                        if score > best_score:
                            best_score = score
                            best_move = [(i, j)]
                        elif score == best_score:
                            best_move.append((i, j))
            # self.print_score_difficult(board)
            if best_score <= 0:
                best_move = random.choice(board.get_empty_positions())
                board.move(best_move[0], best_move[1], self)
            else:
                best_move = random.choice(best_move)
                board.move(best_move[0], best_move[1], self)
            print('Computer move: ', best_move)
            return best_move[0], best_move[1]

        elif self.difficulty == 'easy':
            print('easy_Computer is thinking...')
            best_score = -1
            best_move = []
            for i in range(board.size):
                for j in range(board.size):
                    if board.board[i][j] == '.':
                        score = self.evaluate_position_easy(board, i, j)
                        if score > best_score:
                            best_score = score
                            best_move = [(i, j)]
                        elif score == best_score:
                            best_move.append((i, j))
            # self.print_score_difficult(board)
            if best_score <= 0:
                best_move = random.choice(board.get_empty_positions())
                board.move(best_move[0], best_move[1], self)
            else:
                best_move = random.choice(best_move)
                board.move(best_move[0], best_move[1], self)
            print('Computer move: ', best_move)
            return best_move[0], best_move[1]

        elif self.difficulty == 'medium':
            print('medium_Computer is thinking...')
            best_score = -1
            best_move = []
            for i in range(board.size):
                for j in range(board.size):
                    if board.board[i][j] == '.':
                        score = self.evaluate_position_medium1(board, i, j)
                        if score > best_score:
                            best_score = score
                            best_move = [(i, j)]
                        elif score == best_score:
                            best_move.append((i, j))
            # self.print_score_difficult(board)
            if best_score <= 0:
                best_move = random.choice(board.get_empty_positions())
                board.move(best_move[0], best_move[1], self)
            else:
                best_move = random.choice(best_move)
                board.move(best_move[0], best_move[1], self)
            print('Computer move: ', best_move)
            return best_move[0], best_move[1]

    def evaluate_position_difficult(self, board, x, y):
        ai_score = board.check_game_over_with_assumed_move_new(x, y, self.symbol)
        opponent_symbol = 'X' if self.symbol == 'O' else 'O'
        opponent_score = board.check_game_over_with_assumed_move_new(x, y, opponent_symbol) - 10
        return max(ai_score, opponent_score)

    def evaluate_position_medium1(self, board, x, y):
        ai_score = board.check_game_over_with_assumed_move_medium1(x, y, self.symbol)
        opponent_symbol = 'X' if self.symbol == 'O' else 'O'
        opponent_score = board.check_game_over_with_assumed_move_new(x, y, opponent_symbol) - 10
        return max(ai_score, opponent_score)

    def evaluate_position_easy(self, board, x, y):
        ai_score = board.check_game_over_with_assumed_move_easy(x, y, self.symbol)
        opponent_symbol = 'X' if self.symbol == 'O' else 'O'
        opponent_score = board.check_game_over_with_assumed_move_new(x, y, opponent_symbol) - 10
        return max(ai_score, opponent_score)

    def evaluate_position_medium(self, board, x, y):
        if board.check_game_over_with_assumed_move(x, y, self.symbol):
            score = 100
        else:
            opponent_symbol = 'X' if self.symbol == 'O' else 'O'
            if board.check_game_over_with_assumed_move(x, y, opponent_symbol):
                score = 80
            else:
                score = 0
        return score

    def print_score_difficult(self, board):
        score = np.zeros((board.size, board.size))
        for i in range(board.size):
            for j in range(board.size):
                if board.board[i][j] == '.':
                    score[i][j] = self.evaluate_position_difficult(board, i, j)
        print(score)

    def print_score_medium(self, board):
        score = np.zeros((board.size, board.size))
        for i in range(board.size):
            for j in range(board.size):
                if board.board[i][j] == '.':
                    score[i][j] = self.evaluate_position_medium(board, i, j)
        print(score)



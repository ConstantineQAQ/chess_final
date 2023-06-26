from Board import Board
from Player import ComputerPlayer, Player
import tkinter as tk
import tkinter.messagebox
from tkinter import colorchooser
from PIL import Image, ImageTk
import os

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("五子棋")
        self.geometry("800x800")
        self.board = Board()
        self.player1 = Player('X')
        self.player2 = ComputerPlayer('O', 'difficult')
        self.current_player = None

        # 创建一个新的frame用来放置按钮
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.TOP)

        # 先创建难度选择的按钮
        self.create_difficulty_buttons()

        # 创建先手后手选择的按钮，并放入新的frame
        self.first_button = self.create_button(self.button_frame, "先手", state=tk.DISABLED, command=self.select_first)
        self.first_button.pack(side=tk.LEFT)

        self.second_button = self.create_button(self.button_frame, "后手", state=tk.DISABLED, command=self.select_second)
        self.second_button.pack(side=tk.LEFT)

        image = Image.open("abab3.jpg")
        self.background_image = ImageTk.PhotoImage(image)
        self.canvas = tk.Canvas(self, width=600, height=600)
        self.canvas.create_image(0, 0, image=self.background_image, anchor='nw')
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<Motion>", self.mouse_move)
        self.draw_board()


    def create_difficulty_buttons(self):
        self.easy_button = self.create_button(self.button_frame, "简单", command=lambda: self.select_difficulty('easy'))
        self.easy_button.pack(side=tk.LEFT)

        self.medium_button = self.create_button(self.button_frame, "中等", command=lambda: self.select_difficulty('medium'))
        self.medium_button.pack(side=tk.LEFT)

        self.hard_button = self.create_button(self.button_frame, "困难", command=lambda: self.select_difficulty('difficult'))
        self.hard_button.pack(side=tk.LEFT)

    def create_button(self, frame, text, **kwargs):
        button = tk.Button(frame, text=text, activebackground='red',
                           font=("Times New Roman", 14), **kwargs)
        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)
        return button

    def on_enter(self, e):
        e.widget['background'] = 'lightblue'

    def on_leave(self, e):
        e.widget['background'] = 'SystemButtonFace'

    def select_difficulty(self, difficulty):
        self.player2 = ComputerPlayer('O', difficulty)
        self.easy_button.config(state=tk.DISABLED)
        self.medium_button.config(state=tk.DISABLED)
        self.hard_button.config(state=tk.DISABLED)

        # 选择完难度后，再激活先后手选择的按钮
        self.first_button.config(state=tk.NORMAL)
        self.second_button.config(state=tk.NORMAL)

    def select_first(self):
        self.select_order(self.player1)
        self.first_button.config(state=tk.DISABLED)
        self.second_button.config(state=tk.DISABLED)

    def select_second(self):
        self.select_order(self.player2)
        self.first_button.config(state=tk.DISABLED)
        self.second_button.config(state=tk.DISABLED)

    def select_order(self, player):
        self.current_player = player
        if self.current_player is self.player2:
            self.Ai_move()

    def draw_board(self):
        self.canvas.create_image(0, 0, image=self.background_image, anchor='nw')
        for i in range(15):
            self.canvas.create_line(20 + i * 40, 20, 20 + i * 40, 580)
            self.canvas.create_line(20, 20 + i * 40, 580, 20 + i * 40)
        for i in range(15):
            for j in range(15):
                if self.board.board[i][j] == 'X':
                    self.canvas.create_oval(20 + j * 40 - 15, 20 + i * 40 - 15, 20 + j * 40 + 15, 20 + i * 40 + 15,
                                            fill='black')
                elif self.board.board[i][j] == 'O':
                    self.canvas.create_oval(20 + j * 40 - 15, 20 + i * 40 - 15, 20 + j * 40 + 15, 20 + i * 40 + 15,
                                            fill='white')

    def Ai_move(self):
        if self.current_player == self.player2:
            x, y = self.current_player.make_move(self.board)
            self.draw_board()
            if self.board.check_game_over(x, y, self.current_player):
                self.game_over(self.current_player)
            else:
                self.current_player = self.player1

    def click(self, event):
        if self.current_player == None:
            tkinter.messagebox.showwarning("WARNING","请先选择难度和先后手")
        if self.current_player == self.player1:
            x, y = (event.y - 20 + 20) // 40, (event.x - 20 + 20) // 40
            if self.board.move(x, y, self.current_player):
                self.draw_board()
                if self.board.check_game_over(x, y, self.current_player):
                    self.game_over(self.current_player)
                else:
                    self.current_player = self.player2
                    x, y = self.current_player.make_move(self.board)
                    self.draw_board()
                    if self.board.check_game_over(x, y, self.current_player):
                        self.game_over(self.current_player)
                    else:
                        self.current_player = self.player1

        '''x, y = (event.y - 20 + 20) // 40, (event.x - 20 + 20) // 40
        if self.board.move(x, y, self.current_player):
            self.draw_board()
            if self.board.check_game_over(x, y, self.current_player):
                self.game_over(self.current_player)
            else:
                self.current_player = self.player2
                x, y = self.current_player.make_move(self.board)
                self.draw_board()
                if self.board.check_game_over(x, y, self.current_player):
                    self.game_over(self.current_player)
                else:
                    self.current_player = self.player1'''

    def mouse_move(self, event):
        x, y = (event.y - 20 + 20) // 40, (event.x - 20 + 20) // 40
        if 0 <= x < 15 and 0 <= y < 15 and self.board.board[x][y] == '.':
            self.canvas.delete("mouse_move")
            self.canvas.create_oval(20 + y * 40 - 15, 20 + x * 40 - 15, 20 + y * 40 + 15, 20 + x * 40 + 15, fill='red',
                                    tags="mouse_move")


    def game_over(self, player):
        self.canvas.unbind("<Button-1>")
        name = "玩家" if player.symbol == 'X' else "电脑"
        tkinter.messagebox.showinfo('提示', f"游戏结束. Player {name} wins.")
        user_choice = tkinter.messagebox.askquestion("游戏结束", "你想要重新开始游戏吗？", icon='warning')
        if user_choice == 'yes':
            self.destroy()
            reset_game()
        else:
            quit_game()
            
    def on_difficulty_changed(self, event):
        difficulty = self.difficulty.get()
        self.computer_player.difficulty = difficulty

def reset_game():
    # 重置游戏的代码
    Game()

def quit_game():
    # 退出游戏的代码
    os._exit(0)
    



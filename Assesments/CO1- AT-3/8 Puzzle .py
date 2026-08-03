from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("8-Puzzle Game")

board = [1,2,3,4,5,6,7,8,""]

def shuffle():
    global board
    while True:
        random.shuffle(board)
        if is_solvable(board):
            break
    draw()

def is_solvable(b):
    nums = [x for x in b if x != ""]
    inv = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                inv += 1
    return inv % 2 == 0

buttons = []

def draw():
    for i in range(9):
        buttons[i]["text"] = board[i]

def move(i):
    empty = board.index("")
    if i in [empty-1, empty+1, empty-3, empty+3]:
        if (i==empty-1 and empty%3!=0) or \
           (i==empty+1 and empty%3!=2) or \
           abs(i-empty)==3:
            board[empty], board[i] = board[i], board[empty]
            draw()
            if board == [1,2,3,4,5,6,7,8,""]:
                messagebox.showinfo("Congratulations","Puzzle Solved!")

for i in range(9):
    b = Button(root, width=6, height=3,
               font=("Arial",20),
               command=lambda x=i: move(x))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

Button(root, text="Shuffle", command=shuffle).grid(row=3,column=0,columnspan=3,sticky="we")

shuffle()

root.mainloop()

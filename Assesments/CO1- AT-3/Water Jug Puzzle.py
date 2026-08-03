from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Water Jug Puzzle")

jug1 = 0
jug2 = 0
cap1 = 4
cap2 = 3
target = 2

status = Label(root, font=("Arial", 14))
status.pack(pady=10)

def update():
    status.config(text=f"Jug 1: {jug1}/4 L    Jug 2: {jug2}/3 L")
    if jug1 == target or jug2 == target:
        messagebox.showinfo("Congratulations!", "You solved the Water Jug Puzzle!")

def fill1():
    global jug1
    jug1 = cap1
    update()

def fill2():
    global jug2
    jug2 = cap2
    update()

def empty1():
    global jug1
    jug1 = 0
    update()

def empty2():
    global jug2
    jug2 = 0
    update()

def pour12():
    global jug1, jug2
    amount = min(jug1, cap2 - jug2)
    jug1 -= amount
    jug2 += amount
    update()

def pour21():
    global jug1, jug2
    amount = min(jug2, cap1 - jug1)
    jug2 -= amount
    jug1 += amount
    update()

Button(root, text="Fill Jug 1", width=15, command=fill1).pack(pady=3)
Button(root, text="Fill Jug 2", width=15, command=fill2).pack(pady=3)
Button(root, text="Empty Jug 1", width=15, command=empty1).pack(pady=3)
Button(root, text="Empty Jug 2", width=15, command=empty2).pack(pady=3)
Button(root, text="Pour Jug1 → Jug2", width=15, command=pour12).pack(pady=3)
Button(root, text="Pour Jug2 → Jug1", width=15, command=pour21).pack(pady=3)

update()
root.mainloop()

from tkinter import *
import random

class DiceRoll:
    def __init__(self, window):
        self.window = window
        self.window.configure(bg="black")
        self.window.geometry("550x350")
        self.window.title("Rolling The Dices Game")
        self.window.resizable(0, 0)

        self.dice_dots = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

        # Add label above the Roll button
        self.label = Label(self.window, text="Player 1 Roll the Dice", font=("Helvetica", 15), bg="black", fg="white")
        self.label.pack(pady=10)

        self.roll_button = Button(self.window, text="Roll!", width=10, height=2, font=("Helvetica", 15), bg="aqua", bd=2, command=self.roll_dices)
        self.roll_button.pack(padx=10, pady=15)

        self.a = None
        self.b = None

    def roll_dices(self):
        self.a = random.choice(self.dice_dots)
        self.b = random.choice(self.dice_dots)

        label = Label(self.window, font=("times", 250), bg="black", fg="yellow")
        label.configure(text=f'{self.a}{self.b}')
        label.pack()

        self.window.after(1500,lambda:self.window.destroy())

def ma():
    window = Tk()
    dice_game = DiceRoll(window)
    window.mainloop()

    # Accessing the values of a and b from outside the class
    a = dice_game.a
    b = dice_game.b
    dice_dots = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    for i in range(len(dice_dots)):
        if a==dice_dots[i]:
            a=i+1
    for i in range(len(dice_dots)):
        if b==dice_dots[i]:
            b=i+1
            
    return [a,b]


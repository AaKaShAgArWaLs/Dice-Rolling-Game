from tkinter import *

class IntegerInputWindow:
    def __init__(self, parent):
        self.window = parent
        self.window.configure(bg="black")
        self.window.geometry("550x350")
        self.window.title("Rolling The Dices Game")
        self.window.resizable(0, 0)
        self.label = Label(parent, text="Enter Number Of Rounds:")
        self.label.pack()

        self.entry = Entry(parent)
        self.entry.pack()

        self.submit_button = Button(parent, text="Submit", command=self.close_window)
        self.submit_button.pack()

        self.input_value = None

    def close_window(self):
        try:
            self.input_value = int(self.entry.get())
        except ValueError:
            print("Invalid input. Please enter an integer.")
        self.window.destroy()

def maii():
    root = Tk()
    app = IntegerInputWindow(root)
    root.mainloop()

    # Accessing the input value from outside the class
    input_value = app.input_value
    return input_value

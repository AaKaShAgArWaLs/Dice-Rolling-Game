import tkinter as tk

def res1(a):
    window = tk.Tk()
    window.configure(bg="black")
    window.geometry("550x350")
    window.title("Rolling The Dices Game")
    window.resizable(0, 0)

    label = tk.Label(window, text="Player 1 Won", font=("Helvetica", 18))
    label.pack(pady=20)
    label = tk.Label(window, text=f"With a Score of {a}", font=("Helvetica", 18))
    label.pack(pady=20)
    window.after(3000,lambda:window.destroy())
    window.mainloop()
def res2(a):
    window = tk.Tk()
    window.configure(bg="black")
    window.geometry("550x350")
    window.title("Rolling The Dices Game")
    window.resizable(0, 0)

    label = tk.Label(window, text="Player 2 Won", font=("Helvetica", 18))
    label.pack(pady=20)
    label = tk.Label(window, text=f"With a Score of {a}", font=("Helvetica", 18))
    label.pack(pady=20)
    window.after(3000,lambda:window.destroy())
    window.mainloop()
def res3():
    window = tk.Tk()
    window.configure(bg="black")
    window.geometry("550x350")
    window.title("Rolling The Dices Game")
    window.resizable(0, 0)

    label = tk.Label(window, text="Its a Tie", font=("Helvetica", 18))
    label.pack(pady=20)
    window.after(3000,lambda:window.destroy())
    window.mainloop()


import tkinter as tk
from tkinter import ttk
import datetime


class GUI:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("ドイチェ")

        self.frame = tk.Frame(self.root)

        self.frame.grid(row=0, column=0)

        self.root.mainloop()


def main():
    GUI()
    return


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk
from datetime import datetime


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        master.geometry("800x500")
        master.title("ドイチェ")
        self.pack()

        self.create_wigets()

    def create_wigets(self):
        timeNow = datetime.now()
        showedTime = timeNow.strftime("%H:%M:%S")

        self.mainTime = tk.Label(self, font=("Koruri", "50", "bold"))
        self.mainTime["text"] = showedTime
        self.mainTime.pack()

def main():
    window = tk.Tk()
    app = Application(window)
    app.mainloop()

if __name__ == "__main__":
    main()
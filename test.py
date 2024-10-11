import tkinter as tk
from tkinter import ttk
from datetime import datetime

WIDTH: int = 800
HEIGHT: int = 500


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.after_id = 0

        self.timeNow = datetime.now()
        self.hours = self.timeNow.strftime("%H")
        self.minutes = self.timeNow.strftime("%M")
        self.seconds = self.timeNow.strftime("%S")

        master.geometry(f"{WIDTH}x{HEIGHT}")
        master.title("ドイチェ")
        self.pack()

        self.create_wigets()

    def create_wigets(self):

        self.canvas = tk.Canvas(self.master, width=WIDTH, height=100, bg="lightgreen")
        self.canvas.pack()
        self.canvas.create_text(
            400,
            50,
            text=f"{self.hours}:{self.minutes}:{self.seconds}",
            font=("Koruri", "72", "bold"),
            tag="Time",
            anchor="center",
        )
        self.updateTime()
        # self.mainTime = tk.Label(self, font=("Koruri", "100", "bold"))
        # self.mainTime["text"] = "test"
        # self.mainTime.pack()

    def updateTime(self):
        timeNow = datetime.now()

        hours = timeNow.strftime("%H")
        minutes = timeNow.strftime("%M")
        seconds = timeNow.strftime("%S")

        self.canvas.delete("Time")
        self.canvas.create_text(
            400,
            50,
            text=f"{hours}:{minutes}:{seconds}",
            font=("Koruri", "72", "bold"),
            tag="Time",
            anchor="center",
        )
        self.after_id = self.after(10, self.updateTime)


def main():
    window = tk.Tk()
    app = Application(window)
    app.mainloop()


if __name__ == "__main__":
    main()

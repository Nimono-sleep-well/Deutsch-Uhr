import tkinter as tk
from tkinter import ttk
from datetime import datetime

from translateDeutsch import translateNumber

WIDTH: int = 2560
HEIGHT: int = 1440


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.after_id = 0

        self.timeNow = datetime.now()
        self.hours = int(self.timeNow.strftime("%H"))
        self.minutes = int(self.timeNow.strftime("%M"))
        self.seconds = int(self.timeNow.strftime("%S"))

        master.geometry(f"{WIDTH}x{HEIGHT}")
        master.title("ドイチェ")
        self.pack()

        self.create_wigets()

    def create_wigets(self):

        self.canvas = tk.Canvas(self.master, width=2000, height=300, bg="lightgreen")
        self.canvas.pack()
        self.canvas.create_text(
            1000,
            150,
            text=f"{self.hours}:{self.minutes}",
            font=("Koruri", "72", "bold"),
            tag="Time",
            anchor="center",
        )
        self.canvas2 = tk.Canvas(self.master, width=2000, height=300, bg="lightblue")
        self.canvas2.pack()
        self.canvas2.create_text(
            1000,
            150,
            text=self.seconds,
            font=("Koruri", "72", "bold"),
            tag="Time",
            anchor="center",
        )

        self.updateTime()
        # self.mainTime = tk.Label(self, font=("Koruri", "100", "bold"))
        # self.mainTime["text"] = "test"
        # self.mainTime.pack()

    def updateTime(self):
        setMode = 0
        # 0:offiziell
        # 1:inoffiziell

        timeNow = datetime.now()

        hours = timeNow.strftime("%I")

        minutes = timeNow.strftime("%M")
        seconds = timeNow.strftime("%S")

        self.canvas.delete("Time")
        self.canvas2.delete("Time")

        if int(minutes) == 0:
            self.canvas.create_text(
                1000,
                150,
                text=f"{translateNumber(int(hours))} Uhr",
                font=("Koruri", "72", "bold"),
                tag="Time",
                anchor="center",
            )
        elif int(minutes) == 15:
            self.canvas.create_text(
                1000,
                150,
                text=f"Viertel nach {translateNumber(int(hours))}",
                font=("Koruri", "72", "bold"),
                tag="Time",
                anchor="center",
            )
        elif int(minutes) == 30:
            self.canvas.create_text(
                1000,
                150,
                text=f"halb {translateNumber(int(hours) + 1)}",
                font=("Koruri", "72", "bold"),
                tag="Time",
                anchor="center",
            )
        elif int(minutes) == 45:
            self.canvas.create_text(
                1000,
                150,
                text=f"Viertel vor {translateNumber(int(hours) + 1)}",
                font=("Koruri", "72", "bold"),
                tag="Time",
                anchor="center",
            )
        else:
            if int(minutes) > 0 and int(minutes) <= 20:
                self.canvas.create_text(
                    1000,
                    150,
                    text=f"{translateNumber(int(minutes))} nach {translateNumber(int(hours))}",
                    font=("Koruri", "72", "bold"),
                    tag="Time",
                    anchor="center",
                )
            elif int(minutes) > 20 and int(minutes) < 30:
                self.canvas.create_text(
                    1000,
                    150,
                    text=f"{translateNumber(60 - int(minutes))} vor halb {translateNumber(int(hours) + 1)}",
                    font=("Koruri", "72", "bold"),
                    tag="Time",
                    anchor="center",
                )
            elif int(minutes) > 30 and int(minutes) <= 40:
                self.canvas.create_text(
                    1000,
                    150,
                    text=f"{translateNumber(int(minutes) - 30)} nach halb {translateNumber(int(hours) + 1)}",
                    font=("Koruri", "72", "bold"),
                    tag="Time",
                    anchor="center",
                )
            elif int(minutes) > 40 and int(minutes) < 60:
                self.canvas.create_text(
                    1000,
                    150,
                    text=f"{translateNumber(60 - int(minutes))} vor {translateNumber(int(hours) + 1)}",
                    font=("Koruri", "72", "bold"),
                    tag="Time",
                    anchor="center",
                )

        self.canvas2.create_text(
            1000,
            150,
            text=translateNumber(int(seconds)),
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

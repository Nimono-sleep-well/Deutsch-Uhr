import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        master.title("テキストボックス内容の取得")
        master.geometry("350x150")
        self.pack()

        self.create_widgets()
    def create_widgets(self):
        self.lb =   tk.Label(self)
        self.lb["text"] =   "入力"
        self.lb.pack(side = "top")
        self.en=    tk.Entry(self)
        self.en.pack()
        self.en.focus_set()
        self.bt = tk.Button(self)
        self.bt["text"] = "ボタン"
        self.bt["command"] = self.print_txtval
        self.bt.pack(side = "bottom")

        #フレーム
        self.fr = tk.Frame()
        self.fr.pack()
        self.sc = tk.Scrollbar(self.fr)
        self.sc.pack(side = tk.RIGHT, fill = "y")
        self.tx = tk.Text(self.fr, width = 20, height = 5)
        self.tx.pack()
        self.tx["yscrollcommand"] = self.sc.set
        self.sc["command"]      =   self.tx.yview

    def print_txtval(self):
        val_en = self.en.get()
        self.tx.insert(tk.END, val_en)
        self.tx.insert(tk.END,'\n')

root = tk.Tk()
app = Application(root)
app.mainloop()
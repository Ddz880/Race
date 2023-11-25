from tkinter import *
root = Tk()
WIDTH = 1024
HEIGHT = 600
POS_X = root.winfo_screenmmwidth() // 2 - WIDTH // 2
POS_Y = root.win
root.title("скачки или скачки?")
root.resizable(False, False)
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
root.mainloop()

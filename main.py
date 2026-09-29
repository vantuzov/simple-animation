import tkinter as tk
from datetime import datetime
import math

root = tk.Tk()
root.title("Часы")

canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

style = 0

def clock():
    canvas.delete("all")

    now = datetime.now()

    h = now.hour % 12
    m = now.minute
    s = now.second

    cx, cy = 250, 230

    def line(angle, length, width, color):
        x = cx + length * math.sin(math.radians(angle))
        y = cy - length * math.cos(math.radians(angle))
        canvas.create_line(cx, cy, x, y, fill=color, width=width)

    if style == 0:
        line((h + m / 60) * 30, 100, 8, "white")
        line(m * 6, 140, 5, "white")
        line(s * 6, 160, 2, "red")
    else:
        line((h + m / 60) * 30, 90, 12, "cyan")
        line(m * 6, 140, 8, "lime")
        line(s * 6, 170, 3, "magenta")

clock()
root.mainloop()

import tkinter as tk
from datetime import datetime
import math

root = tk.Tk()
root.title("Часы")

canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

style = 0
running = False
start = 0


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

    canvas.create_oval(
        cx - 5, cy - 5,
        cx + 5, cy + 5,
        fill="white"
    )

    canvas.create_text(
        250, 450,
        text=now.strftime("%d.%m.%Y"),
        fill="white",
        font=("Arial", 16)
    )

    phases = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]
    phase = phases[(now.day // 4) % 8]

    canvas.create_text(
        250, 480,
        text="Луна " + phase,
        fill="white",
        font=("Arial", 18)
    )

    root.after(1000, clock)


def change_style():
    global style
    style = 1 - style


def chrono_start():
    global running, start

    if not running:
        start = datetime.now()
        running = True
        chrono()


def chrono_stop():
    global running
    running = False


def chrono_reset():
    global running
    running = False
    chrono_label.config(text="00:00")


def chrono():
    if running:
        t = datetime.now() - start
        chrono_label.config(
            text=str(t.seconds).zfill(2)
        )
        root.after(100, chrono)


tk.Button(
    root,
    text="Сменить стрелки",
    command=change_style
).pack()

chrono_label = tk.Label(
    root,
    text="00:00",
    font=("Arial", 18)
)
chrono_label.pack()

tk.Button(root, text="Старт", command=chrono_start).pack(side="left")
tk.Button(root, text="Стоп", command=chrono_stop).pack(side="left")
tk.Button(root, text="Сброс", command=chrono_reset).pack(side="left")

clock()
root.mainloop()

import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
count_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(count_timer)
    canvas.itemconfig(timer, text="00:00")
    title_label.config(text="Title", fg=GREEN)
    check_mark.config(text=" ")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def call_counter():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=PINK)
    elif reps % 2 == 1:
        title_label.config(text="Work", fg=RED)
        count_down(work_sec)
    else:
        title_label.config(text="Break", fg=GREEN)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global count_timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # dynamic typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")  # update the counter on the canvas
    if count > 0:
        count_timer = window.after(1000, count_down, count - 1)  # a timer
    else:
        call_counter()
        number = math.floor(reps / 2)
        mark = ""
        for _ in range(number):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomatoes")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill='white')
canvas.grid(row=1, column=1)

title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50), highlightthickness=0)
title_label.grid(row=0, column=1)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"), highlightthickness=0)
check_mark.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

start_button = Button(text="Start", highlightthickness=0, command=call_counter)
start_button.grid(row=2, column=0)

window.mainloop()

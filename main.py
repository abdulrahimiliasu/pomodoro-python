from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
    text_timer.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'normal'))
    checkmark_text.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_min = WORK_MIN * 60
    shor_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 == 0:
        text_timer.config(text="Rest", bg=YELLOW, fg=RED, font=(FONT_NAME, 40, 'normal'))
        count_down(shor_break_min)
    elif reps % 8 == 0:
        text_timer.config(text="Rest", bg=YELLOW, fg=PINK, font=(FONT_NAME, 40, 'normal'))
        count_down(long_break_min)
    else:
        text_timer.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'normal'))
        count_down(work_min)

# ---------------------------- COUNTDOWN MECHANISM -------------------------------


def count_down(count):
    minutes = math.floor(count/60)
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer, text=f"{minutes}:{secs}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += CHECKMARK
        checkmark_text.config(text=marks)

# ---------------------------- UI SETUP -------------------------------


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text_timer = Label(text="Timer")
text_timer.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'normal'))
text_timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=img)
timer = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_bttn = Button(text="Start")
start_bttn.config(bg=YELLOW, highlightthickness=0, command=start_timer)
start_bttn.grid(row=2, column=0)

reset_bttn = Button(text="Reset")
reset_bttn.config(bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_bttn.grid(row=2, column=2)

checkmark_text = Label()
checkmark_text.config(bg=YELLOW, fg=GREEN,)
checkmark_text.grid(row=3, column=1)

window.mainloop()

from tkinter import *
from tkinter import font
import focusSteal # gives top window focus

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
SECONDS = 4

# ---------------------------- ATRIBUTE CLASS ------------------------------- #
class Values:
    ''' Number of repitions and var for storing command after's return ID'''
    def __init__(self):
        self.reps = 0
        self.after_id = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    
    turn.reps = 0
    start_button["state"] = "active"
    window.after_cancel(turn.after_id)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    
    turn.reps +=1
    work_sec =WORK_MIN * SECONDS # runs on 1,3 odd times etc
    break_short = SHORT_BREAK_MIN * SECONDS # runs 2,4, evens, 
    long_break = LONG_BREAK_MIN * SECONDS # runs on 8th time
    
    focusSteal.raise_above_all(window)
    
    if turn.reps % 8 == 0:
        title_label.config(text='Long break',fg=RED)
        count_down(long_break)
    elif turn.reps % 2 == 0:
        title_label.config(text='Short break',fg=PINK)
        count_down(break_short)
    else:
        title_label.config(text='Do work!!',fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    start_button["state"] = "disabled"
    start_button["disabledforeground"] = start_button["foreground"]

    count_minutes = (count // 60)
    count_seconds = count % 60
    canvas.itemconfig(timer_text,text=f'{count_minutes:02d}:{count_seconds:02d}')

    if count > 0:
        turn.after_id = window.after(10,count_down,count-1)
    else:
        start_timer()
    marks=''
    for _ in range(turn.reps//2):
        marks += '✔'
        check_marks.config(text=marks)
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50,bg=YELLOW)


title_label= Label(text='Timer',width=11, bg=YELLOW,fg=GREEN,font=(FONT_NAME,50))
title_label.grid(column=1, row=0)

'''create  canvas of the tomato picture with a second text canvas on top'''
canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130,text='00:00', fill='white',font=(FONT_NAME,35,'bold'))
window.iconphoto(False, tomato_img)  # Creates window icon
canvas.grid(column=1,row=1)

start_button = Button(text='Start',highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset',highlightthickness=0,command= reset_timer)
reset_button.grid(column=2,row=2)

check_marks = Label(bg=YELLOW,fg=GREEN) # blank label

check_marks.grid(column=1, row=3)


#-----main-----
turn = Values()
window.mainloop()
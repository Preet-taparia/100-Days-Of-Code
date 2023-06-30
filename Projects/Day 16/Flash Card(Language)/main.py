import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


def datarandom():
    unknown1 = random.choice(data)
    return unknown1


def change_red():
    global flip_timer
    window.after_cancel(flip_timer)
    unknown1 = datarandom()
    canvas.itemconfig(main_image, image=image1)
    canvas.itemconfig(main_text, text="Hindi", fill="black")
    canvas.itemconfig(text, text=unknown1["Hindi"], fill="black")
    flip_timer = window.after(3000, show)


def change_green():
    global flip_timer
    window.after_cancel(flip_timer)
    unknown1 = datarandom()
    canvas.itemconfig(main_image, image=image1)
    canvas.itemconfig(main_text, text="Hindi", fill="black")
    canvas.itemconfig(text, text=unknown1["Hindi"], fill="black")
    flip_timer = window.after(3000, show)
    data.remove(unknown1)
    new = pd.DataFrame(data)
    new.to_csv("data/words_to_learn.csv", index=False)


def show():
    unknown1 = datarandom()
    canvas.itemconfig(main_image, image=image4)
    canvas.itemconfig(text, text=unknown1["English"], fill="white")
    canvas.itemconfig(main_text, text="English", fill="white")


try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/hindi_words.csv",encoding="UTF-8")
finally:
    data = data.to_dict(orient="records")

window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=30, pady=30)
image1 = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
main_image = canvas.create_image(400, 263, image=image1)
main_text = canvas.create_text(400, 150, text="Hindi", font=("Ariel", 40, "italic"))
text = canvas.create_text(400, 263, text=random.choice(data)["Hindi"],  font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
image4 = PhotoImage(file="images/card_back.png")

image2 = PhotoImage(file="images/right.png")
button1 = Button(image=image2, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=change_green)
button1.grid(row=1, column=1)

image3 = PhotoImage(file="images/wrong.png")
button2 = Button(image=image3, highlightthickness=0, borderwidth=0, command=change_red)
button2.grid(row=1, column=0)
flip_timer = window.after(3000, show)
window.mainloop()


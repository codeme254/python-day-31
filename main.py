BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
from pandas import *
from random import choice
import pandas
win = Tk()
win.title("Flashy")
win.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
title = "Title"
word = "Word"

front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas()
canvas.config(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=front_image)
canvas.create_text(400, 150, fill="crimson", text="Title", font=("Verdana", 40, "italic"), tag="title")
card_word = canvas.create_text(400, 263, fill="crimson", text="Word", font=("Verdana", 60, "bold"), tag="text")
canvas.grid(column=0, row=0, columnspan=2)

# buttons
wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")
button_unknown = Button(image=wrong_image, highlightthickness=0)
button_unknown.grid(column=0, row=1)
button_known = Button(image=right_image, highlightthickness=0)
button_known.grid(column=1, row=1)

data = pandas.read_csv("./data/french_words.csv")
data_list = data.to_dict(orient='records')


def configure_canvas_texts(main_word, language):
    canvas.delete("text")
    canvas.delete("title")
    canvas.create_text(400, 150, fill="crimson", text=language, font=("Verdana", 40, "italic"), tag="title")

    canvas.create_text(400, 263, fill="crimson", text=main_word, font=("Verdana", 60, "bold"), tag="text")

def generate_random_word():
    current_word = choice(data_list)
    french_word = current_word['French']
    english_word = current_word['English']
    canvas.create_image(400, 263, image=front_image)
    configure_canvas_texts(main_word=french_word, language="French")
    def flip_card():
        canvas.create_image(400, 263, image=back_image)
        configure_canvas_texts(main_word=english_word, language="English")
    win.after(3000, flip_card)

generate_random_word()
button_known.config(command=generate_random_word)
button_unknown.config(command=generate_random_word)

win.mainloop()

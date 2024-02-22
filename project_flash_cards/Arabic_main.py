from bs4 import BeautifulSoup
import requests
from tkinter import *
import pandas as pd
import random


# -------------Extra file from internet -----------------------------
def extract(url, row, column_name, deli):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table_titles = soup.find_all(row)[41:177]
    world_table_titles = [title.text.strip() for title in table_titles]
    df = pd.DataFrame(world_table_titles, columns=['word'])
    df[column_name] = df['word'].str.split(deli, n=1, expand=True)
    df.to_csv('data/Arabic_words.csv', header=True)


extract(url='https://www.fluentin3months.com/arabic-words',
        row='li',
        column_name=['English', 'Arabic'],
        deli="–")
# -------------------------------------------------------------------------------------------

BACKGROUND_COLOR = "#B1DDC6"
new_word = {}
words = {}
try:
    data = pd.read_csv("./data/arabic_words_to_learn")
except FileNotFoundError:
    data = pd.read_csv("./data/Arabic_words.csv")
    words = data.to_dict(orient='records')
else:
    words = data.to_dict(orient='records')


def next_word():
    global new_word, flip_timer
    canvas.after_cancel(flip_timer)
    new_word = random.choice(words)
    canvas.itemconfig(card_title, text="Arabic", fill='black')
    canvas.itemconfig(card_text, text=new_word['Arabic'], fill='black')
    canvas.itemconfig(front_canvas, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_text, text=new_word['English'], fill='white')
    canvas.itemconfig(front_canvas, image=card_back_image)


def remove_word():
    words.remove(new_word)
    file = pd.DataFrame(words)
    file.to_csv("data/arabic_words_to_learn", index=False)


# -----------------------------------------UI----------------------------------
window = Tk()
window.title("Flasy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
front_canvas = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 130, text="", font=("Ariel", 35, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 45, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
next_word()

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_word)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=remove_word)
wrong_button.grid(row=1, column=1)
window.mainloop()

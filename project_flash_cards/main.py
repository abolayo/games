from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flasy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0)

card_back_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_back_image)
canvas.grid(row=0, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)

window.mainloop()

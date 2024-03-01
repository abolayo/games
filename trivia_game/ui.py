from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.score = None
        self.quiz = quiz_brain
        self.window = Tk()

        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}", fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, highlightthickness=1, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            120,
            width=270,
            fill=THEME_COLOR,
            text="Welcome",
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.right_button = Button(
            image=true_img,
            highlightthickness=0,
            command=self.use_true
        )
        self.right_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(
            image=false_image,
            highlightthickness=0,
            command=self.use_false
        )
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_question():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
            bye = f"You've completed the quiz\nYour final score is {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question_text, text=bye)
            self.window.after(2000, exit)

    def use_true(self):
        self.give_feedback(self.quiz.check_answer('true'))

    # line 58==61,62
    def use_false(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



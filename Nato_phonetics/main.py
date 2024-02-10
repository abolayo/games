import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
game = True
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
while game:
    letter_word = list(input("Enter a word: ").upper())

    if letter_word == list('X'):
        print("Bye!!!")
        game = False
    else:
        try:
            output = [nato_dict[letter] for letter in letter_word]

        except KeyError:
            print("Sorry, only letters in the alphabet please!")
        else:
            print(output)

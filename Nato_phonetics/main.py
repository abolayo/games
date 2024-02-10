import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
game = True
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generative_phonetics():
    letter_word = list(input("Enter a word: ").upper())
    try:
        output = [nato_dict[letter] for letter in letter_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        generative_phonetics()
    else:
        print(output)


generative_phonetics()

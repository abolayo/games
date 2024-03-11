import pandas as pd
PLACEHOLDER = '[name]'
# Getting the names from the file

df = pd.read_csv("./Input/Names/names.csv")
names = df['name'].to_list()
with open("./Input/Letters/starting_letter.txt", "r") as file:
    letters = file.read()
    for name in names:
        name_clean = (name.strip())
        new_letter = letters.replace(PLACEHOLDER, name_clean)
    print(new_letter)
    # # # # Save completed letter in the folder
    #     with open(f"./ReadyToSend/{name}.txt", "w") as final_letter:
    #
    #         final_letter.writelines(new_letter)

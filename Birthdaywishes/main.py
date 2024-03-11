#PLACEHOLDER = "[name]"
# # Getting the names from the file
# with open("Input/Names/names.csv", "r") as names:
#     names = names.readlines()
#
# with open("./Input/Letters/starting_letter.txt", "r") as file:
#     letters = file.read()
#     for name in names:
#         name = (name.strip())
#         new_letter = letters.replace(PLACEHOLDER, name)
#
#     # # # Save completed letter in the folder
#         with open(f"./ReadyToSend/{name}.txt", "w") as final_letter:
#
#             final_letter.writelines(new_letter)
import pandas as pd

df = pd.read_csv("./Input/Names/names.csv")
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
print(df.head())
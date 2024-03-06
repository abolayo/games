PLACEHOLDER = "[name]"
# # Getting the names from the file
with open("Input/Names/names.txt", "r") as names:
    names = names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as file:
    letters = file.read()
    for name in names:
        name = (name.strip())
        new_letter = letters.replace(PLACEHOLDER, name)

    # # # Save completed letter in the folder
        with open(f"./ReadyToSend/{name}.txt", "w") as final_letter:
            final_letter.writelines(new_letter)

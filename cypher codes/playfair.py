import numpy as np
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
key = input('please enter the key text : ').upper()
new_alphabet = []
for letter in key:
    if letter == "I" or letter == "J":
        letter = "I"
    alphabet.remove(letter)
    new_alphabet += letter
new_alphabet += alphabet
new_alphabet = np.reshape(new_alphabet, (5, 5))
print(new_alphabet)
text = input('please enter the key text : ').upper()
c_text = []

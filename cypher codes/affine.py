alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
a = int(input('please enter the first key :'))
b = int(input('please enter the second key :'))
text = input('please enter the text : ').upper()
c_text = []
enc = int(input("press 1 for encryption and any number for decryption :"))
def affine(t,k1,k2,is_e):
    for letter in text:
        index = text.index(letter)
        if enc == 1:
            c_text.append((a*alphabet.index(letter) + b) % 26)
        else:
            c_text.append((pow(a, -1, 26)*(alphabet.index(letter) - b)) % 26)
        c_text[index] = alphabet[c_text[index]]
    return c_text

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
text = input('please enter the text you want to encrypt : ').upper
key = int(input('please enter the key : '))
is_enc = int(input("enter 1 to encryption an any number to decryption : "))
def AutoKey(k, is_e , t) :
    c_text = []
    for letter in t() :
        num = alphabet.index(letter) 
        if is_e == 1 :
            c_text.append(alphabet[num+k%26])
        else : 
            c_text.append(alphabet[num-k%26])
        k = num 
    return c_text
print(*AutoKey(key,is_enc,text))
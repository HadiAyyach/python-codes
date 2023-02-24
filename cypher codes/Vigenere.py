alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cipher_text = []
def vigenere(key, p_text, enc):
    c_text =[]
    main_index = 0
    k_len = len(key())
    for letter in p_text():
        letter_num = alphabet.index(letter)
        
        #                                       mod key 
        key_num = alphabet.index(key()[main_index%k_len])
        if enc == 1 :
            c_text.append(alphabet[(letter_num+key_num)%26])
        else :
            c_text.append(alphabet[(letter_num-key_num)%26])
        main_index += 1
    return c_text    
platte_text = input('please enter the text : ').upper
key = input("please enter the key : ").upper
is_enc = int(input("enter 1 to encryption an any number to decryption : "))
print(*vigenere(key,platte_text,is_enc))

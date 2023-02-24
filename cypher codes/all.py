import numpy as np
# the alphabet
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def affine(t,is_e):
    c_text = []
    k1 = int(input('please enter the first key as a number:'))
    k2 = int(input('please enter the second key as a number :'))
    index = 0
    for letter in t:
        if is_e == 1:
            #             key1 *the number of letters + key2
            c_text.append((k1*alphabet.index(letter) + k2) % 26)
        else:
            #              key1(inverse)  *the number of letters  - key2
            c_text.append((pow(k1, -1, 26)*(alphabet.index(letter) - k2)) % 26)
        #turn the numbers into letters 
        c_text[index] = alphabet[c_text[index]]
        index += 1
    return c_text

def AutoKey(t,is_e) :
    c_text = []
    # takeing the key
    k =int(input('please enter the key as a number : '))
    for letter in t :
        # the number of the letter
        num = alphabet.index(letter) 
        if is_e == 1 :
            # just adding the key and the number of letter and append it
            c_text.append(alphabet[num+k%26])
        else : 
            c_text.append(alphabet[num-k%26])
        # the new key is the last number of letter 
        k = num 
    return c_text

def vigenere( t, is_e):
    c_text =[]
    k = input("please enter the key as a letters : ").upper
    main_index = 0
    for letter in t:
        letter_num = alphabet.index(letter)
        # convert the letter into a number and loop it if its short 
        key_num = alphabet.index(k()[main_index%(len(k()))])
        if is_e == 1 :
            c_text.append(alphabet[(letter_num+key_num)%26])
        else :
            c_text.append(alphabet[(letter_num-key_num)%26])
        main_index += 1
    return c_text    

def Hill(t,is_e):
    c_text = []
    k = []
    # takeing the key array and save it
    for i in range(4):
        k.append(int(input(f'please enter the key number {i} : ')))
    main_index = 0
    # reshaping the key to 2d array
    k = np.reshape(k, (2,2))
    letters_mat = []
    c_mat = []
    # chick if its encryption or decryption
    if is_e != 1 :
        # the determiner 
        det = pow(int(np.linalg.det(k)),-1,26)
        # inverse the key in old way 
        temp = k[0,0]
        k[0,0] = k[1,1]
        k[1,1] = temp
        k[0,1] = k[0,1]*-1
        k[1,0] = k[1,0]*-1
        k = k%26
        k = k*det%26
    for letter in t:
        # convert to numbers
        letters_mat.append(alphabet.index(letter))
        # make sure there is tow numbers in the array
        if (main_index+1)%2 == 0 :
            # multiply the key with the array 
            c_mat.append(np.matmul(k,letters_mat)%26)
            # empty the array 
            letters_mat.pop()
            letters_mat.pop()
        main_index += 1
    # convert 2d array into 1d array 
    c_mat  = np.array(c_mat)
    c_mat = c_mat.flatten()
    # convert it to letters 
    for num in c_mat :
        c_text.append(alphabet[int(num)])
    return c_text

# get the inputs
is_enc = int(input('please enter 1 for encryption and any other number for decryption : '))
p_text = input('please enter the text : ').upper()
algorithm = int(input("enter the algorithm you want to use : \n 1 : for affine \n 2 : for AutoKey \n 3 : for Vigenere \n 4 : for Hill \n : "))
# choosing the algorithm
if algorithm == 1 :
    print(*affine(p_text, is_enc))
elif algorithm == 2 :
    print(*AutoKey(p_text, is_enc))
elif algorithm == 3 :
    print(*vigenere(p_text, is_enc))
elif algorithm == 4 :
    print(*Hill(p_text, is_enc))
else :
    print('wrong input baby :) ')
    
    
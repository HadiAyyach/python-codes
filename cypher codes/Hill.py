import numpy as np
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
text = input('please enter the text you want to encrypt : ').upper
key = []
for i in range(4):
    key.append(int(input(f'please enter the key number {i} : ')))
is_enc = int(input("enter 1 to encryption an any number to decryption : "))
def Hill(k,t,is_e):
    c_text = []
    main_index = 0
    k = np.reshape(k, (2,2))
    letters_mat = []
    c_mat = []
    if is_e != 1 :
        det = pow(int(np.linalg.det(k)),-1,26)
        print(det)
        # invers the matrix 
        temp = k[0,0]
        k[0,0] = k[1,1]
        k[1,1] = temp
        k[0,1] = k[0,1]*-1
        k[1,0] = k[1,0]*-1
        k = k%26
        k = k*det%26
    for letter in t():
        letters_mat.append(alphabet.index(letter))
        if (main_index+1)%2 == 0 :
            c_mat.append(np.matmul(k,letters_mat)%26)
            letters_mat.pop()
            letters_mat.pop()
        main_index += 1
    c_mat  = np.array(c_mat)
    c_mat = c_mat.flatten()
    for num in c_mat :
        c_text.append(alphabet[int(num)])
    return c_text
print(*Hill(key,text,is_enc))
                       
        
        
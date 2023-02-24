from typing import List
def allSameCase(word: str) -> bool:
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    counter = 0
    for i in word :
        if i in alphabet :
            counter += 1
        else :
            counter += 10
    return counter == len(word) or counter == len(word)*10
        
from typing import List
def missingLetter(txt: str) -> str:
    txt = txt.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    start = alphabet.index(txt[0])
    for i in txt :
        if i != alphabet[start] : 
            return alphabet[start]
        start += 1
    return 'No Missing Letter'
print(missingLetter('vwyz'))
from typing import List
def arrowDuplicates(word: str) -> str:
    word = word.lower()
    result = ""
    for i in word :
        if word.count(i) != 1 :
           result += '<'
        else :
           result += '>'
    return result
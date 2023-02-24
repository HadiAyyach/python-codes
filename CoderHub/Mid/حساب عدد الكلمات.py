from typing import List
def countWords(txt: str) -> int:
    # write your code here ^_^
    result = 0
    for i in txt :
        if i == " " :
            result += 1 
    return result +1

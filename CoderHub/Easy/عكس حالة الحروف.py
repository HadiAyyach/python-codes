from typing import List
def reverse_case(strParam: str) -> str:
    lowercase = 'qwertyuiopasdfghjklzxcvbnm'
    result = ''
    for letter in strParam :
        if letter in lowercase :
            result += letter.upper()
        else :
            result += letter.lower()
    return result
            
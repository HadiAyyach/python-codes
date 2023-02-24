from typing import List
def hasSpace(strParam: str) -> str:
    result = ''
    for i in strParam :
        if i == ' ' :
            result += '#'
        else :
            result += i
    return result
            
from typing import List
def countDown(number: int) -> str:
    result = str(number)
    number -= 1
    while number >= 0 :
        result += ' '
        result += str(number)
        number -= 1
    return result
        
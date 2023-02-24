from typing import List
def left_digit(strParam: str) -> int:
    numbers = '0','1','2','3','4','5','6','7','8','9'
    for digit in strParam :
        if digit in numbers:
            return int(digit)


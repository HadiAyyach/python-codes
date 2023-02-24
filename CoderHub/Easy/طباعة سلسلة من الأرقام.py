from typing import List
def numbers_range(number: int) -> str:
    result = '0'
    for i in range(1,number + 1):
        result += ' '+str(i)
    return result
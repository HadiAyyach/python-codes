from typing import List
def number_sum(num: int) -> int:
    result = 0
    for i in range(1,num+1):
        result += i
    return result
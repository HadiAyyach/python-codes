from typing import List
def sumOdd(arr: List[int]) -> int:
    sum = 0
    for i in arr:
        if i % 2 == 1:
            sum += i
    return sum
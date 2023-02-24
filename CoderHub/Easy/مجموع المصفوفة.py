from typing import List
def calculate_sum(lst: List[int]) -> int:
    result = 0
    if lst.count(7) != 0:
        for i in lst[:lst.index(7)]:
            result += i
    else:
        for i in lst:
            result += i
    return result
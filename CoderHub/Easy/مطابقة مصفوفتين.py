from typing import List
def match_arrays(array1: List[str], array2: List[str]) -> bool:
    result = True
    if len(array1) != len(array2):
        return False
    for i in array1:
        found = False
        for j in array2:
            if i == j:
                found = True
                break
        result = result and found
    return result
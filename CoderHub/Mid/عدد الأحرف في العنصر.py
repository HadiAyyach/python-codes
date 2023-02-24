from typing import List
def word_length(arr: List[str]) -> List[int]:
    arr_num = []
    for i in arr:
        arr_num.append(len(i))
    return arr_num
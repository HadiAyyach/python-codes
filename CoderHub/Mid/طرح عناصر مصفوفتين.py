from typing import List
def sub_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    result = []
    for i in range(len(arr1)):
        result.append(arr2[i] -arr1[i])
    return result 
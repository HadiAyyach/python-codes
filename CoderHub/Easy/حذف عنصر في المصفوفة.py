from typing import List
def delete_element_in_array(arr: List[int], index: int) -> List[int]:
    result = arr
    result.remove(result[index])
    return result
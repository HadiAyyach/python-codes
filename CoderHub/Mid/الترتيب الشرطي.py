from typing import List
def namesSort(namesArray: List[str], order: str) -> List[str]:
    if order == 'ASC' :
        namesArray.sort()
    elif order == 'DESC' :
        namesArray.sort(reverse=True)
    return namesArray
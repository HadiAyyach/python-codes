from typing import List
def root_check(sqr: float, num: int) -> int:
    if num*num == sqr:
        return num
    else:
        return 0
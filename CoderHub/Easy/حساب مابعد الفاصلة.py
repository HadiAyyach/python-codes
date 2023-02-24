from typing import List
def Decimal_places(num: str) -> int:
    if num.count('.') == 0:
        return 0
    else:
        return len(num[num.index('.')+1:])    
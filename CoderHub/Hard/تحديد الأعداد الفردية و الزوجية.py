from typing import List
def oddsVsEvens(num: int) -> str:
    odd_sum = 0
    even_sum = 0
    num = str(num)
    for i in num :
        if int(i) % 2 == 0 :
            even_sum += int(i)
        else :
            odd_sum += int(i)
    if even_sum < odd_sum :
        return 'odd'
    elif even_sum == odd_sum :
        return 'equal'
    else :
        return 'even'
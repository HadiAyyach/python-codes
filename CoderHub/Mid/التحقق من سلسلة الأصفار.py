from typing import List
def longestZero(strParam: str) -> str:
    count_list = []
    sync = False
    for digit in strParam :
        if digit == '0' :
            if sync :
                count_list[len(count_list)-1] += 1
            else :
                sync = True
                count_list.append(1)
        else:
            sync = False
    result = ''
    for i in range(max(count_list)):
        result +='0'
    return result



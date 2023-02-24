from typing import List
def cap_space(txt: str) -> str:
    caps = "QWERTYUIOPASDFGHJKLZXCVBNM"
    result = ''
    for v in txt:
        if v in caps :
            result += ' ' + v.lower()
        else:
            result += v
    return result
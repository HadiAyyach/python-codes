from typing import List
def say_hi_bye(name: str, num: int) -> str:
    if num == 0:
        return 'Bye ' + name
    elif num == 1:
        return 'Hi ' + name
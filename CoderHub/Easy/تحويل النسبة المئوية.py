from typing import List
def convertPercent(percentage: str) -> float:
    number = float(percentage[:-1])
    return number*0.01
print(convertPercent('3%'))
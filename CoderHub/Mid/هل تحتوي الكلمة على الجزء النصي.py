from typing import List
def stringContains(firstName: str, contains: str) -> bool:
    if contains in firstName:
        return True
    else:
        return False
firstName = 'Sara'
contains = 's'
print(stringContains(firstName, contains))
from typing import List
def getPrimesBetween(a: int, b: int) -> List[int]:
    result = []
    for i in range(a,b+1):
        if i < 2 :
            continue
        is_prime = True
        for j in range(2,i):
            if  i % j == 0:
                is_prime = False
                break

        if is_prime:
            result.append(i)
    return result
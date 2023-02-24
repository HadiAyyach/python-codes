from typing import List
def factorial(number: int) -> int:
    result = 1
    for i in range(number):
        result *= i+1
    return result
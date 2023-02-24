from typing import List
def word_repeat(word: str, n: int) -> str:
    result = word
    for i in range(n-1):
        result += ' ' + word
    return result
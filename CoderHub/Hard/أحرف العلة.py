from typing import List
def first_n_vowels(phrase: str, n: int) -> str:
    letters = 'a', 'e', 'i','o','h','A', 'I', 'E', 'O', 'H','u', 'U'
    all_vowels = []
    for letter in phrase :
        if letter in letters :
            all_vowels.append(letter)
    if n > len(all_vowels) :
        return 'invalid'
    all_vowels = all_vowels[:n]
    return ''.join(all_vowels)


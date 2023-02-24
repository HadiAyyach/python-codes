from typing import List
def find_prefix(words: List[str], text: str) -> List[str]:
    result = []
    for i in words:
        if text.lower() == i[:len(text)].lower():
            result.append(i)
    if len(result) == 0:
        return ['No matches found']
    return result
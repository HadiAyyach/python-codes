from typing import List
def replaceThe(txt: str) -> str:
    result = txt
    vaowls = 'h','i','o','e','a','u'
    while True:
        if 'the' in result:
            if result[result.index('the')+4] in vaowls:
                result = result.replace('the','an',1)
            else:
                result = result.replace('the','a',1)
        else:
            break
    return result
print(replaceThe('im the hadi the king'))
from typing import List
def isEmail(email: str) -> bool:
    sympole = '.',',',':','?','=','-','(',')','"','\'','/','%','@','!'
    if sympole.count(email[0]) != 0 :
        return 0
    if email.count('@') == 0 :
        return 0
    elif email.index('@') == 0 :
        return 0
    atindex = email.index('@')
    if email[atindex:].count('.') == 0 :
        return 0
    elif email[atindex +1] == '.' :
        return 0
    if email[atindex:].index('.') + len(email[:atindex]) + 3 > len(email) :
        return 0
    return 1
email = 'example@example.com','example@example.c','example@com','@example.com'
for e in email :
    print(bool(isEmail(e)))
    

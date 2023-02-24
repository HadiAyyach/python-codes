from typing import List
def oct_to_bin(octal: int) -> str:
    dec = 0
    octal = str(octal)
    index = 0
    base = pow(8,len(octal)-1)
    while index != len(octal) :
        dec += int(octal[index]) * int(base)
        index += 1
        base /= 8
    return str(bin(dec))[2:]
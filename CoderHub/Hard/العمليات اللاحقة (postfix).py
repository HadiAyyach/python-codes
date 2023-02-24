from typing import List
def postFix(expr: str) -> int:
    ops = '/*-+'
    nums = []
    op = []
    for i in expr.split(' '):
        if i in ops :
            op.append(i)
        else:
            nums.append(i)
    statement = nums[0] 
    nums.pop(0)
    for j in range(len(nums)) :
        statement += op[0]
        statement += nums[0]
        op.pop(0)
        nums.pop(0)
        statement = str(eval(statement))
    return int(float(statement))
from typing import List
def math_expr(expr: str) -> bool:
    rest_nums= False
    there_op = False
    operation = '/','*','-','+'
    for i in expr:
        if i in operation:
            there_op = True
            expr = expr.replace(i,'')
    try:
        if int(expr) is not None:
            rest_nums = True
    except ValueError:
        return False
    return rest_nums and there_op
class Solution(object):
    def addBinary(self, a, b):
        while len(a) != len(b):
            if len(a) < len(b): a= '0'+ a
            else: b = '0'+ b
        reseat = False
        result = ''

        for i in range(len(a)):
            if a[-i-1] == b[-i-1]:
                if reseat:
                    if a[-i-1] == '1': result = '1'+ result
                    else: result = '1'+ result ; reseat = False 
                else:
                    if a[-i-1] == '1': reseat = True 
                    result = '0'+ result
            else:
                if reseat:result = '0'+ result
                else: result = '1'+ result ; reseat = False
        if reseat:result = '1'+ result
        return result
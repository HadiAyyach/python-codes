class Solution(object):
    def addToArrayForm(self, num, k):
        number = ''
        for i in num:
            number += str(i)
        result = int(number)+ k
        res= []
        for i in str(result):
            res.append(int(i))
        return res
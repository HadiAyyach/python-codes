class Solution(object):
    def plusOne(self, digits):
        number = ''
        for i in digits:
            number += str(i)
        result = int(number)+ 1
        res= []
        for i in str(result):
            res.append(int(i))
        return res
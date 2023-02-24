class Solution(object):
    def invalidTransactions(self, transactions):
        result = []
        final_result = []
        for i , v in enumerate( transactions):
            if v in result: continue
            v = v.split(',')
            if int(v[2]) > 1000 :
                if i not in result :result.append(i)
            for j , u in enumerate(transactions[i+1:],i+1):
                u = u.split(',')
                if v[0] == u[0] and abs(int(v[1]) - int(u[1])) <= 60 and v[3] != u[3]:
                    if i not in result :result.append(i)
                    if j not in result :result.append(j)
        for i in result :
            final_result.append(transactions[i])
        return final_result
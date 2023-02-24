class Solution(object):
    def twoSum(self, nums, target):
        result = []
        done = False
        for i,v in enumerate(nums):
            for j,u in enumerate(nums[i+1:],i+1):
                if u + v == target :
                    result.append(i)
                    result.append(j)
                    done = True
                    break
            if done:
                break
        return result
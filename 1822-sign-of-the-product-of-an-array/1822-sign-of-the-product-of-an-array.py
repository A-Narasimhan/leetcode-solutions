class Solution:
    def arraySign(self, nums: list[int]) -> int:
        count = 0
        for n in nums:
            if n == 0:
                return 0
            if n<0:
                count+=1
        if count % 2 != 0:
            return -1
        else:
            return 1
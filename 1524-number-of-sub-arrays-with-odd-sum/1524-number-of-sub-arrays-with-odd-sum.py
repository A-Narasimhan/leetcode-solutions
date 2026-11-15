class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        prefix = 0
        odd = 0
        even = 1
        count = 0
        for num in arr:
            prefix += num
            if prefix&1:
                odd+=1
                count+=even
            else:
                even+=1
                count+=odd
        return count%(10**9+7)
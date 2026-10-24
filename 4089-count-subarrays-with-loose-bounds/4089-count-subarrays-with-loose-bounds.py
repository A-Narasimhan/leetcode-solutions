class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        ans = 0
        last_invalid = -1
        for i,x in enumerate(nums):
            if x<minK or x>maxK:
                last_invalid = i
            ans += i - last_invalid
        return ans

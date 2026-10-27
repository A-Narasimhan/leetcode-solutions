class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_,n = 0,len(nums)
        for i in range(n):
            max_ = max(max_,nums[i])
            nums[i] = gcd(nums[i],max_)
        nums.sort()
        return sum(gcd(nums[i],nums[~i]) for i in range(n//2))

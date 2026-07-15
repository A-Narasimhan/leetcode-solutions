class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxNonAdjacentSum(arr):
            prev1 = arr[0]
            prev2 = 0
            
            for i in range(1,len(arr)):
                take = arr[i]
                if i>1:
                    take+=prev2
                not_take = 0 + prev1

                curr = max(take,not_take)
                prev2 = prev1
                prev1 = curr
            return prev1

        n = len(nums)

        if n == 1:
            return nums[0]
        temp1 = nums[1:]
        temp2 = nums[:-1]

        return max(maxNonAdjacentSum(temp1),maxNonAdjacentSum(temp2))
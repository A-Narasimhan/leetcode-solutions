
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        # Count how many numbers contain each bit.
        count = [0] * 31

        for num in nums:
            for bit in range(31):
                if num & (1 << bit):
                    count[bit] += 1

        # Construct k maximum numbers.
        ans = 0

        for _ in range(k):
            num = 0

            for bit in range(30, -1, -1):
                if count[bit] > 0:
                    num |= (1 << bit)
                    count[bit] -= 1

            ans = (ans + num * num) % MOD

        return ans

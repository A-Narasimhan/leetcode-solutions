class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_moves = min(nums)
        return sum(x - min_moves for x in nums)
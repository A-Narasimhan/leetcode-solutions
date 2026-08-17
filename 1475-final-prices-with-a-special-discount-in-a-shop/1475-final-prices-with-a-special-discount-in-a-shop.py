class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices.copy()
        stack = []
        for i,price in enumerate(prices):
            while stack and prices[stack[-1]]>=price:
                prev_i = stack.pop()
                ans[prev_i] -= price
            stack.append(i)
        return ans
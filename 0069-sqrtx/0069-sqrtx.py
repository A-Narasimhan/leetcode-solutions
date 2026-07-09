class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l = 1
        high = x
        ans = 0
        while l<=high:
            mid = l+(high-l)//2
            square = mid*mid
            if square == x:
                return mid
            elif square<x:
                ans = mid
                l = mid+1
            else:
                high = mid-1
        return ans
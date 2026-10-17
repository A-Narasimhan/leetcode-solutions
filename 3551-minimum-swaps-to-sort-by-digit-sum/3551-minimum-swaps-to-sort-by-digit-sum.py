class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        b = sorted(nums,key = lambda v : (sum(map(int,str(v))),v))
        d , res = dict(zip(nums,count())),0
        for v,u in zip(nums,b):
            if v != u: nums[d[u]],d[v],res = v,d[u],res+1
        return res
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
       sSum = sum(ord(c) for c in s)
       tSum = sum(ord(c) for c in t)
       return chr(tSum - sSum)
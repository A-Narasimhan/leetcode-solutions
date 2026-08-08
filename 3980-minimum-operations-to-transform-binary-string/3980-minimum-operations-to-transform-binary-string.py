class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        n = len(s1)
        if n == 1:
            if s1 == s2:
                return 0
            if s1 == "0" and s2 == "1":
                return 1
            return -1
        i = ans = 0
        while i<n:
            if s1[i] == "0" and s2[i] == "1":
                ans+=1
                i+=1
            elif s1[i] == "1" and s2[i] == "0":
                length = 0
                while i<n and s1[i] == "1" and s2[i] == "0":
                    length += 1
                    i+=1
                ans+=3*((length+1)//2)-length
            else:
                i+=1
        return ans
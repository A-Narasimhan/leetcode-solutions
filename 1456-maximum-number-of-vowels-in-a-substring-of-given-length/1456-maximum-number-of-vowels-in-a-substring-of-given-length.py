class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_ = count = 0
        n = len(s)
        for i in range(n):
            if i >= k and s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            max_ = max(max_,count)
        return max_
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev_w = [word[::-1] for word in words]
        return ' '.join(rev_w)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        combined = s + "#" + rev

        lps = [0] * len(combined)
        length = 0

        for i in range(1, len(combined)):
            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]

            if combined[i] == combined[length]:
                length += 1
                lps[i] = length

        longest = lps[-1]
        return rev[:len(s) - longest] + s

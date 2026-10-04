class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0 #minimum possible number of unmatched (
        high = 0 #maximum possible number of unmatched (

        for c in s:

            if c == '(':
                low += 1
                high += 1

            elif c == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1      # treat * as ')'
                high += 1     # treat * as '('

            if high < 0:
                return False

            if low < 0:
                low = 0

        return low == 0
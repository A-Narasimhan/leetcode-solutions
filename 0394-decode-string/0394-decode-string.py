class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k*10+int(char)
            elif char == '[':
                stack.append((curr_str,k))
                curr_str = ""
                k = 0
            elif char == ']':
                prev_str,rep_cnt = stack.pop()
                curr_str = prev_str+curr_str*rep_cnt
            else:
                curr_str += char
        return curr_str
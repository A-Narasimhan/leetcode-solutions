class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1 if n == 1 else 1

        s = [1, 2, 2]

        i = 2
        num = 1
        count = 1

        while len(s) < n:
            length = s[i]

            for _ in range(length):
                if len(s) == n:
                    break
                s.append(num)

                if num == 1:
                    count += 1

            num = 3 - num
            i += 1

        return count
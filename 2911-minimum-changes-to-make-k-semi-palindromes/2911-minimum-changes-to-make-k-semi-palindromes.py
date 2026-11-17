
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute minimum changes for every substring
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = float('inf')

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for r in range(d):
                        count = (length - 1 - r) // d + 1

                        for t in range(count // 2):
                            left = i + r + t * d
                            right = i + r + (count - 1 - t) * d

                            if s[left] != s[right]:
                                changes += 1

                    best = min(best, changes)

                cost[i][j] = best

        # DP: dp[i][p] = minimum changes to partition
        # first i characters into p substrings
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for prev in range(2 * (p - 1), i - 1):
                    dp[i][p] = min(
                        dp[i][p],
                        dp[prev][p - 1] + cost[prev][i - 1]
                    )

        return dp[n][k]

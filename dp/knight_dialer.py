class Solution:
    def knightDialer(self, N: int) -> int:
        mod = 10**9 + 7
        nbrs = {
            0:(4, 6), 1:(6, 8), 2:(7, 9), 3:(4, 8), 4:(0, 3, 9),
            5:(), 6:(0, 1, 7), 7:(2, 6), 8:(1, 3), 9:(2, 4)
        }

        dp = [1] * 10
        for _ in range(N - 1):
            dp2 = [0] * 10
            for key, count in enumerate(dp):
                for nbr in nbrs[key]: dp2[nbr] += count
            dp = dp2

        return sum(dp) % mod


class Solution2:
    def knightDialer(self, N: int) -> int:
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1

        for _ in range(N - 1):
            x1, x2, x3, x4, x5 = x6 + x8, x7 + x9, x4 + x8, x3 + x9 + x0, 0,
            x6, x7, x8, x9, x0 = x1 + x7 + x0, x2 + x6, x1 + x3, x2 + x4, x4 + x6

        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10**9 + 7)


# 935. Knight Dialer
# https://leetcode.com/problems/knight-dialer/solution/

# Intuition:
# model:
# dp2[i] represents the number of strings generated by starting from source key 'i',
# dp[i] represents the previous level's dp results
# recurrence relation:
# dp2[dst_key] = dp2[dst_key] + dp[src_key]

# Steps:
# 1. Given the number of hops
# 2. We have an array 'dp' of size 10, indexed from 0...9 representing the keys of the phone
# 3. We iterate for each hop, we use the results from the previous hop (dp) to generate
#    the number of strings (phone number strings) generated starting from every key
# 4. Meaning to get total number of strings for 5 hops, we use strings representing ways of getting to i from length 4 hops
#    and from various source keys for every i in [0, 9]
# 5. At the end, we return the sum of dp, distinct strings formed by starting from each source key

# Example: N = 3
# dp: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# HOP 1
# dp2: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], nbr: 4
# dp2: [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], nbr: 6

# dp2: [0, 0, 0, 0, 1, 0, 2, 0, 0, 0], nbr: 6
# dp2: [0, 0, 0, 0, 1, 0, 2, 0, 1, 0], nbr: 8

# dp2: [0, 0, 0, 0, 1, 0, 2, 1, 1, 0], nbr: 7
# dp2: [0, 0, 0, 0, 1, 0, 2, 1, 1, 1], nbr: 9

# dp2: [0, 0, 0, 0, 2, 0, 2, 1, 1, 1], nbr: 4
# dp2: [0, 0, 0, 0, 2, 0, 2, 1, 2, 1], nbr: 8

# dp2: [1, 0, 0, 0, 2, 0, 2, 1, 2, 1], nbr: 0
# dp2: [1, 0, 0, 1, 2, 0, 2, 1, 2, 1], nbr: 3
# dp2: [1, 0, 0, 1, 2, 0, 2, 1, 2, 2], nbr: 9

# dp2: [2, 0, 0, 1, 2, 0, 2, 1, 2, 2], nbr: 0
# dp2: [2, 1, 0, 1, 2, 0, 2, 1, 2, 2], nbr: 1
# dp2: [2, 1, 0, 1, 2, 0, 2, 2, 2, 2], nbr: 7

# dp2: [2, 1, 1, 1, 2, 0, 2, 2, 2, 2], nbr: 2
# dp2: [2, 1, 1, 1, 2, 0, 3, 2, 2, 2], nbr: 6

# dp2: [2, 2, 1, 1, 2, 0, 3, 2, 2, 2], nbr: 1
# dp2: [2, 2, 1, 2, 2, 0, 3, 2, 2, 2], nbr: 3

# dp2: [2, 2, 2, 2, 2, 0, 3, 2, 2, 2], nbr: 2
# dp2: [2, 2, 2, 2, 3, 0, 3, 2, 2, 2], nbr: 4

# HOP 2
# dp: [2, 2, 2, 2, 3, 0, 3, 2, 2, 2]
# dp2: [0, 0, 0, 0, 2, 0, 0, 0, 0, 0], nbr: 4
# dp2: [0, 0, 0, 0, 2, 0, 2, 0, 0, 0], nbr: 6

# dp2: [0, 0, 0, 0, 2, 0, 4, 0, 0, 0], nbr: 6
# dp2: [0, 0, 0, 0, 2, 0, 4, 0, 2, 0], nbr: 8

# dp2: [0, 0, 0, 0, 2, 0, 4, 2, 2, 0], nbr: 7
# dp2: [0, 0, 0, 0, 2, 0, 4, 2, 2, 2], nbr: 9

# dp2: [0, 0, 0, 0, 4, 0, 4, 2, 2, 2], nbr: 4
# dp2: [0, 0, 0, 0, 4, 0, 4, 2, 4, 2], nbr: 8

# dp2: [3, 0, 0, 0, 4, 0, 4, 2, 4, 2], nbr: 0
# dp2: [3, 0, 0, 3, 4, 0, 4, 2, 4, 2], nbr: 3
# dp2: [3, 0, 0, 3, 4, 0, 4, 2, 4, 5], nbr: 9

# dp2: [6, 0, 0, 3, 4, 0, 4, 2, 4, 5], nbr: 0
# dp2: [6, 3, 0, 3, 4, 0, 4, 2, 4, 5], nbr: 1
# dp2: [6, 3, 0, 3, 4, 0, 4, 5, 4, 5], nbr: 7

# dp2: [6, 3, 2, 3, 4, 0, 4, 5, 4, 5], nbr: 2
# dp2: [6, 3, 2, 3, 4, 0, 6, 5, 4, 5], nbr: 6

# dp2: [6, 5, 2, 3, 4, 0, 6, 5, 4, 5], nbr: 1
# dp2: [6, 5, 2, 5, 4, 0, 6, 5, 4, 5], nbr: 3

# dp2: [6, 5, 4, 5, 4, 0, 6, 5, 4, 5], nbr: 2
# dp2: [6, 5, 4, 5, 6, 0, 6, 5, 4, 5], nbr: 4


sol = Solution()
assert sol.knightDialer(1) == 10
assert sol.knightDialer(2) == 20
assert sol.knightDialer(3) == 46
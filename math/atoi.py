class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if not ls: return 0

        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']: ls.pop(0)
        result, i = 0, 0

        while i < len(ls) and ls[i].isdigit():
            result = result * 10 + ord(ls[i]) - ord('0')
            i += 1

        return max(-2**31, min(sign * result, 2**31-1))


# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

# Approach 1
# 1. Strip input and get chars in an array
# 2. capture sign and delete the sign from array start
# 3. process each char that is a digit
# 4. and add to integer result (ret * 10 + str digit.ord)
# 5. as soon as we encounter a non-digit exit and return the result
# 6. Ensure there is no overflow at the return of result. Has to be 32 bit integer.

# Approach 2: Refer java file with same name
# DFA
# 1. keep track of all the valid states
# 2. Define valid transitions
# 3. as soon as we hit an invalid state
# 4. return the signed current integer value

# Time: O(n)
# Space: O(n), to store ls array

sol = Solution()
assert sol.myAtoi("-1 2 3 4") == -1
assert sol.myAtoi("+-2") == 0
assert sol.myAtoi("-1") == -1
assert sol.myAtoi("-0012a42") == -12
assert sol.myAtoi("   +0 123") == 0
assert sol.myAtoi("123  456") == 123
assert sol.myAtoi("   - 321") == 0
assert sol.myAtoi("    010") == 10

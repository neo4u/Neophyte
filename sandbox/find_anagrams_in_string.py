import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not p or len(p) > len(s): return []

        p_hash = collections.Counter(p)
        m, n, desired, formed = len(s), len(p), len(p_hash), 0
        s_hash = collections.defaultdict(int)
        result = []

        for j in range(n):
            c = s[j]
            s_hash[c] += 1
            if c in p_hash and p_hash[c] == s_hash[c]: formed += 1

        if formed == desired: result.append(0)

        r = n
        while r < m:
            l = r - n + 1 # get 1st char in n size window
            lc, rc = s[l - 1], s[r]

            if lc in p_hash and p_hash[lc] == s_hash[lc]: formed -= 1
            s_hash[lc] -= 1

            s_hash[rc] += 1
            if rc in p_hash and p_hash[rc] == s_hash[rc]: formed += 1

            if formed == desired: result.append(l)
            r += 1

        return result



# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

# 'aabc' 'abc'

# formed = 2
# desired = 3


# "aab"
# {
#     a: 1
#     b: 1
        
# }

# "ab"

# { a:1
#   b:1 
# }

# "cbaebabacd"
# "abc"
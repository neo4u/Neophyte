class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        b_idx = 0

        while n:
            buf4 = [''] * 4
            count_read = read4(buf4)
            if not count_read: break

            for j in range(min(count_read, n)):
                buf[b_idx] = buf4[j]
                b_idx += 1
                n -= 1

        return b_idx


# 157. Read N Characters Given Read4
# https://leetcode.com/problems/read-n-characters-given-read4/

# I think the most confusing thing is the example given by the problem description,
# according to the solution, *buf is destination buffer.
# (https://en.wikipedia.org/wiki/Data_buffer).
# That means whenever we call read4(buf),
# 4 consecutive characters from the file are copied into the *buf buffer array.
# So the example of this problem is not the following:

# Input: buf = "abc", n = 4
# Output: "abc"
# Explanation: The actual number of characters read is 3, which is "abc".
# Instead, it should be:

# Given a file = "abc", and a destination buffer, buf = ["", "", "", ..... ]
# after calling read(buf, 4), we will have: output = 3
# and the destination buffer becomes buf = ["a", "b", "c", "", "", "", .......]
# Because the read(buf, 4) function copied 4 characters (but there are only 3 in the file) from the file into the destination buffer

# Approach
# 1. maintain a pointer for 1 more than last index of buffer, this will be the final return
# 2. capture read4 into buf4 of length 4
# 3. copy over buf4 into read4, while decrementing n and incrementing buffer index
# 4. the tricky part is when at the end only < 4 chars are returned
# 5. At that point take min of return count and remaining n and copy over the chars from buff for those many times

# Time: O(n)
# Space: O(1)

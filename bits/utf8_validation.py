from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # Number of bytes in the current UTF-8 character
        n_bytes = 0

        # Mask to check if the most significant bit (8th bit from the left) is set or not
        mask1 = 1 << 7

        # Mask to check if the second most significant bit is set or not
        mask2 = 1 << 6
        for num in data:

            # Get the number of set most significant bits in the byte if
            # this is the starting byte of an UTF-8 character.
            mask = 1 << 7
            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1

                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:

                # If this byte is a part of an existing UTF-8 character, then we
                # simply have to look at the two most significant bits and we make
                # use of the masks we defined before.
                if not (num & mask1 and not (num & mask2)):
                    return False

            n_bytes -= 1

        return n_bytes == 0


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n_bytes = 0
        mask1, mask2 = 1 << 7, 1 << 6

        for num in data:
            mask = 1 << 7

            if n_bytes == 0: # Header byte
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1

                if not n_bytes: continue
                if n_bytes not in {2, 3, 4}: return False
            else:           # Every other byte
                if not (num & mask1 and not num & mask2): return False

            n_bytes -= 1

        return n_bytes == 0


# 393. UTF-8 Validation
# https://leetcode.com/problems/utf-8-validation/description/


# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

# For 1-byte char, the first bit is a 0, followed by its unicode code.
# For n-bytes chars, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.

# This is how the UTF-8 encoding works:
# Char. number range  |        UTF-8 octet sequence
#    (hexadecimal)    |              (binary)
# --------------------+---------------------------------------------
# 0000 0000-0000 007F | 0xxxxxxx
# 0000 0080-0000 07FF | 110xxxxx 10xxxxxx
# 0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
# 0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx


# Steps:
# 1. There are two types of bytes
#    - One type is the header byte indicating the number of following bytes
#    - Other type is the following byte which starts with b'10'
# 2. We use a n_bytes var to distinguish the above 2 conditions
# 3. If n_bytes == 0, then it means we've encountered a header byte
#    - when its a header byte we, set n_bytes by counting the number of leading bits
# 4. if n_bytes != 0, then it means we've encountered a non-header byte

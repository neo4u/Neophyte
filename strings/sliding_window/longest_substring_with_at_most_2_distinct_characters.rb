# @param {String} s
# @return {Integer}
def length_of_longest_substring_two_distinct(s)
    return 0 if !s || s.empty?      # Corner case
    return s.size if s.size <= 2    # Trivial case

    map = Array.new(128, 0)         # O(1)
    # left and right bounds for window (l and r),
    # longest length of string to return as result (longets),
    # counter for number of elements in the window,
    # replace s with the an array of bytes for the characters
    l, r, longest, counter = 0, 0, 0, 0 
    s = s.bytes

    while r < s.size
        counter += 1 if map[s[r]] == 0
        map[s[r]] += 1
        r += 1

        while counter > 2
            map[s[l]] -= 1
            counter -= 1 if map[s[l]] == 0
            l += 1
        end
        longest = [longest, r - l].max
    end

    longest
end

# 159. Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

# Approach 1: Use sliding window
# 1. Fix pointers l, r to 0
# 2. Keep expanding r to next char and see if it breaks the utmost 2 chars property
# 3. If it breaks keep kicking out an instance of a char (from window)
#    and increment left pointer until at most 2 chars
# 4. If it doesn't break keep expanding window by incrementing right pointer
#    and incrementing map of counts for each char

# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(length_of_longest_substring_two_distinct('eceba'), 3)
assert_equal(length_of_longest_substring_two_distinct('ccaabbb'), 5)
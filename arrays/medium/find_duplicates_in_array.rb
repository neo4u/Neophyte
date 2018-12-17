# @param {Integer[]} nums
# @return {Integer[]}
def find_duplicates(nums)
    p nums
    puts
    res = []
    nums.each do |x|
        i = x.abs - 1
        nums[i] < 0 ? res.push(x.abs) : nums[i] = -nums[i]
    end

    res
end

# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

# Approach 1: Hash
# Approach 2: Two Pass
# 1. Since numbers are non-negative and range is 1 <= num <= size of array, we can mark duplicates as -ve
# 2. Iterate through the array, For each num we find the index corresponding to that integer for n, i = n - 1
# 3. We add the abosolute value of the current number x to result if nums[i] < 0 (this means it was marked -ve alr)
# 4. If not we mark the number at index as -ve, to mark that we've seen this number once

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_duplicates([4,3,2,7,8,2,3,1]), [2,3])

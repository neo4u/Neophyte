# @param {Integer[]} nums
# @return {Integer}
def rob(nums)
    return 0 if nums.empty?
    return nums.max if nums.size <= 2
    n = nums.size
    dp = [-1] * n
    dp[0], dp[1] = nums[0], [nums[0], nums[1]].max

    2.upto(n - 1) do |i|
        dp[i] = [dp[i - 1], dp[i - 2] + nums[i]].max
    end

    dp[n - 1]
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(rob([]), 0)
assert_equal(rob([0, 0, 0]), 0)
assert_equal(rob([1, 1, 1]), 2)
assert_equal(rob([1, 1]), 1)

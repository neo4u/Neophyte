# @param {Integer[]} digits
# @return {Integer[]}
def plus_one(digits)
    n, carry = digits.size, 1
    (n - 1).downto(0) do |i|
        if digits[i] < 9
            digits[i] += 1
            return digits
        end
        carry, digits[i] = (digits[i] + carry).divmod(10)
    end
    digits.unshift(carry) unless carry.zero?

    digits
end

# 66. Plus One
# https://leetcode.com/problems/plus-one/description/

# 1. Use a carry, that starts out as 1
# 2. Keep adding the carry and digit at current index
# 3. After exhausting all the digits, check if carry and
#    append it from the front of list


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(plus_one([0]), [1])
assert_equal(plus_one([9]), [1, 0])

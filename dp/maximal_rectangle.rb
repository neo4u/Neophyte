# @param {Character[][]} matrix
# @return {Integer}
def maximal_rectangle(matrix)
    return 0 if !matrix || !matrix[0]
    max_area, n = 0, matrix[0].size()
    heights = Array.new(n, 0)
    
    matrix.each do |row|
        0.upto(n - 1) do |i|
            # Only extend the value if the column contains a '1' value else reset to 0
            heights[i] = row[i] == '1' ? heights[i] + 1 : 0
        end
        max_area = [max_area, largest_rectangle_area(heights)].max
    end

    max_area
end

# Runs in O(n)
def largest_rectangle_area(heights)
    heights << -1
    max_area, n, stack = 0, heights.size(), []

    0.upto(n - 1) do |i|
        while !stack.empty? && heights[i] < heights[stack.last]
            h = heights[stack.pop()]
            w = stack.empty? ? i : i - 1 - stack.last
            max_area = [max_area, h * w].max
        end
        stack.push(i)
    end

    max_area
end

# https://leetcode.com/problems/maximal-rectangle/description/
# 85. Maximal Rectangle
# Time: O(n^2)
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

arr = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
assert_equal(maximal_rectangle(arr), 6)
arr = [['1']]
assert_equal(maximal_rectangle(arr), 1)
arr = [["0", "1"], ["1", "0"]]
assert_equal(maximal_rectangle(arr), 1)
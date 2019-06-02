# Definition for an interval.
class Interval
    attr_accessor :start, :end
    def initialize(s=0, e=0)
        @start = s
        @end = e
    end
end

# @param {Interval[]} intervals
# @param {Interval} new_interval
# @return {Interval[]}
def insert(intervals, new_interval)
    return [new_interval] if !intervals || intervals.empty?
    return intervals if !new_interval
    n = intervals.size

    # The map below is essentially just doing what is being done in the below code, but concisely without storing permanent variables
    # starts, ends = Array.new(n), Array.new(n)
    # 0.upto(n - 1) do |i|
    #     starts[i] = intervals[i].start
    #     ends[i] = intervals[i].end
    # end

    # If we can't find elements in the array that match the criteria (bsearch returns nil), choose n as the index
    # Before bsearch we're doing to_a as bsearch only works on Array and not on Enumerator type, map however works on enumerator type
    i = intervals.each_with_index.map.to_a.bsearch { |e, _| e.end > new_interval.start }&.last || n # equivalent to bisect_left in python, O(log(n))
    j = intervals.each_with_index.map.to_a.bsearch { |s, _| new_interval.end <= s.start  }&.last || n # equivalent to bisect_right in python, O(log(n))

    new_interval.start = [new_interval.start, intervals[i].start].min if i < n  # We merge new_int's start with interval[i]'s start,
                                                                                # i because, all intervals < index i don't have any overlap with the new_intvl, overlap can only occur in ith inteval,
                                                                                # because of the condition e >= new_interval.start while doing a binary search
    new_interval.end = [new_interval.end, intervals[j - 1].end].max if 0 < j    # We merge new_int's end with intervals[j - 1]'s end,
                                                                                # j - 1 because, intervals with index j and greater don't have any overlap with the new_intvl

    left = intervals[0...i]
    right = intervals[j...n]

    left + [new_interval] + right # O(n), stiching the arrays together
end

# [[1, 4], [8, 10]], [5, 6]
# i = 1
# j = 1

# [5, 6]
# [1, 4] + [5, 6] + [8, 10]

# 1,4] [7, 8]  [4,5]

# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# i = 1
# j = 4

# new_interval = [3, 10]
# l = [1, 2] + [3, 10] + [12, 16]




# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

# Approach 1: Binary Search on starts and ends arrays
# Steps
# 1. Binary Search ends for e >= new_interval.start, i.e. Find the index i into intervals where all the ends to the left of i are < new_interval.start
# 2. Binary Search starts for s > new_interval.end, i.e. Find the index into intervals where all the starts to the right of i are > new_interval.start
# 3. Use n if there is no such index for both the searches
# 4. Merge new_interval's start with interval i's start
# 5. Merge new_interval's end with interval j - 1's end
# 6. Final form the left part, middle part and right part
# 6. Return the combination of the tree parts

# Example 1: intervals = [1, 3], [6, 9] new = [2, 5]
# starts: [1, 6] | ends: [3, 9]
# i: 0 | j: 1
# left: [] | new_interval: [1, 5] | right: [6, 9]

# Example 2: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] new = [4,8]
# starts: [1, 3, 6, 8, 12] | ends: [2, 5, 7, 10, 16]
# i: 1 | j: 4
# left: [1,2] | new_interval: [3, 10] | right: [12, 16]

# Example 3: intervals = [[1,5]] new = [2,3]
# starts: [1] | ends: [5]
# i: 0 | j: 1
# left: [] | new_interval: [1,5] | right: []

# Example 4: intervals = [[1,2],[6,9]] new = [3,5]
# starts: [1, 6] | ends: [2, 9]
# i: 1 | j: 1
# left: [1,2] | new_interval: [3,5] | right: [6,9]

# Time: O(n)
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

# intervals = [
#     Interval.new(1,3),
#     Interval.new(6,9)
# ]
# new_interval = Interval.new(2,5)
# output = insert(intervals, new_interval)

# assert_equal(output[0].start, 1)
# assert_equal(output[0].end, 5)
# assert_equal(output[1].start, 6)
# assert_equal(output[1].end, 9)

# intervals = [
#     Interval.new(1,2),
#     Interval.new(3,5),
#     Interval.new(6,7),
#     Interval.new(8,10),
#     Interval.new(12,16)
# ]
# new_interval = Interval.new(4,8)
# output = insert(intervals, new_interval)
# [
#     Interval.new(1,2),
#     Interval.new(3,10),
#     Interval.new(12,16)
# ]
# assert_equal(output[0].start, 1)
# assert_equal(output[0].end, 2)
# assert_equal(output[1].start, 3)
# assert_equal(output[1].end, 10)
# assert_equal(output[2].start, 12)
# assert_equal(output[2].end, 16)

# intervals = [
#     Interval.new(1,5),
# ]
# new_interval = Interval.new(2,3)
# output = insert(intervals, new_interval)
# assert_equal(output[0].start, 1)
# assert_equal(output[0].end, 5)

# intervals = [
#     Interval.new(1,2),
#     Interval.new(6,9)
# ]
# new_interval = Interval.new(3,5)
# output = insert(intervals, new_interval)
# assert_equal(output[0].start, 1)
# assert_equal(output[0].end, 2)
# assert_equal(output[1].start, 3)
# assert_equal(output[1].end, 5)
# assert_equal(output[2].start, 6)
# assert_equal(output[2].end, 9)

# [1, 4] [7, 9]   [4 6]


# 1 4] 4 6  
intervals = [
    Interval.new(1,4),
    Interval.new(7,9)
]
new_interval = Interval.new(4,6)
output = insert(intervals, new_interval)
assert_equal(output[0].start, 1)
assert_equal(output[0].end, 4)
assert_equal(output[1].start, 4)
assert_equal(output[1].end, 6)
assert_equal(output[2].start, 7)
assert_equal(output[2].end, 9)
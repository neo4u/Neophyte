# Approach 1: Using queue
class MovingAverage
    def initialize(size)
        @window = []
        @size = size.to_f
        @avg = 0
        @sum = 0
    end

    def next(val)
        @window.push(val)                   # Push incoming val into queue
        @sum += val                         # Add to sum

        if @window.size <= @size
            @avg = @sum / @window.size.to_f # keep calculating the average
        else
            @sum -= @window.shift()         # Kick out one elemnt from the sum
            @avg = @sum / @size.to_f        # Then calculate the average
        end

        @avg
    end
end


# Approach 2: Using %
class MovingAverage
    attr_accessor :sum, :size, :queue, :head

    def initialize(size)
        @sum = 0.0
        @size = size
        @queue = Array.new(size, 0)
        @head = 0
    end

    def next(val)
        @sum -= @queue[head % size]
        @sum += val
        @queue[head % size] = val
        @head += 1
        @sum / [head, size].min
    end
end

# 346. Moving Average from Data Stream
# https://leetcode.com/problems/moving-average-from-data-stream/description/

# Approach 1: 
# Steps:
# 1. 
# 2. 


require 'test/unit'
extend Test::Unit::Assertions

m = MovingAverage.new(3)
assert_equal(m.next(1), 1.0)
assert_equal(m.next(10), 5.5)
assert_equal(m.next(3), 4.666666666666667)
assert_equal(m.next(5), 6.0)

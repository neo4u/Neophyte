# Definition for an interval.
# class Interval
#     attr_accessor :start, :end
#     def initialize(s=0, e=0)
#         @start = s
#         @end = e
#     end
# end

# @param {Interval[]} intervals
# @return {Integer}
def min_meeting_rooms(intervals)
    return 0 if !intervals || intervals.empty?
    used_rooms, n = 0, intervals.size
    starts, ends = Array.new(n), Array.new(n)
    0.upto(n - 1) do |i|
        starts[i] = intervals[i].start
        ends[i] = intervals[i].end
    end

    starts.sort!
    ends.sort!
    s_ptr, e_ptr = 0, 0

    while s_ptr < n
        if starts[s_ptr] >= ends[e_ptr]
            used_rooms -= 1
            e_ptr += 1
        end
        s_ptr += 1
        used_rooms += 1
    end

    used_rooms
end

# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/

# Approach 1: Sort by start times and use Priority Queue for end times.
# Refer to the python code from same file name in directory with .py

# Approach 2: Keep independent array of start and end times, inc ment for each start and dec when curr_start >= curr_end
# Algorithm
# 1. Separate out the start times and the end times in their separate arrays.
# 2. Sort the start times and the end times separately. Note that this will mess up the original correspondence of start times and end times. They will be treated individually now.
# 3. We consider two pointers: s_ptr and e_ptr which refer to start pointer and end pointer. The start pointer simply iterates over all the meetings and the end pointer helps us track if a meeting has ended and if we can reuse a room.
# 4. When considering a specific meeting pointed to by s_ptr, we check if this start timing is greater than the meeting pointed to by e_ptr. If this is the case then that would mean some meeting has ended by the time the meeting at s_ptr had to start. So we can reuse one of the rooms. Otherwise, we have to allocate a new room.
# 5. If a meeting has indeed ended i.e. if start[s_ptr] >= end[e_ptr], then we increment e_ptr.
# 6. Repeat this process until s_ptr processes all of the meetings.

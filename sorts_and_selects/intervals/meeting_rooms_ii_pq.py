# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x.start)

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0].end)

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i.start:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i.end)

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

# Algorithm
# 1. Sort the given meetings by their start time.
# 2. Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
# 3. For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
# 4. If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
# 5. If not, then we allocate a new room and add it to the heap.
# 6. After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.

# Complexity Analysis

# Time Complexity: O(NlogN). There are two major portions that take up time here.
#                  One is sorting of the array that takes O(NlogN) considering that the array consists of N elements.
#                  Then we have the min-heap. In the worst case, all N meetings will collide with each other.
#                  In any case we have N add operations on the heap. In the worst case we will have N extract-min operations as well.
#                  Overall complexity being (NlogN) since extract-min operation on a heap takes O(logN).
# Space Complexity: O(N) because we construct the min-heap and that can contain N elements
#                   in the worst case as described above in the time complexity section.
#                   Hence, the space complexity is O(N). 
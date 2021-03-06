from heapq import heappush, heappop
import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time, q = 0, []
        for v in collections.Counter(tasks).values():
            heappush(q, -v) # Use negatives to get max heap

        while q:
            cool_timer, temp = 0, []
            while cool_timer <= n and (q or temp): # q is empty or but we have cooling to do cuz there are items in temp
                time += 1
                cool_timer += 1                              # keep incrementing the cooling timer

                if q:
                    x = heappop(q)
                    if x < -1: temp.append(x + 1)   # >= -1 means, the task was completed, else dec frequency and add to temp for next round
            for item in temp: heappush(q, item)     # push all pending task frequencies onto maxheap (min heap with -ve values)
                                                    # or ADT priority queue (hence the variable name q)
        return time


# CLEANER VERSION OF ABOVE CODE
from collections import Counter
from heapq import heappush, heappop, heapify

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        q = [-v for v in Counter(tasks).values()]
        heapify(q)

        while q:
            cool, temp = n + 1, []

            while cool > 0 and (q or temp):
                time += 1
                cool -= 1
                if q:
                    x = -heappop(q) -1
                    if x > 0: temp.append(-x)
            if temp:
                q.extend(temp)
                heapify(q)

        return time


# Approach 3: Calculating the idle slots, Time: O(n), Space: O(1)
class Solution2(object):
    # O(n) # of the most frequent tasks, say longest, will determine the legnth
    # to avoid counting idle intervals, we count (longest - 1) * (n + 1)
    # then count how many will in the last cycle which means finding ties
    # if counted number is less than # of tasks which means 
    # less frequent tasks can be always placed in such cycle
    # and it won't cause any conflicts with requirement since even most frequent can be settle
    # finally, return max(# of task, total counted number)
    def leastInterval(self, tasks, n):
        d = collections.Counter(tasks)
        counts = d.values()
        longest = max(counts)
        ans = (longest - 1) * (n + 1)

        for count in counts:
            if count == longest: ans += 1

        return max(len(tasks), ans)


# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/

# Approach 1: Using sorting Time: O(time), Space: O(1)
# Not implemented, as internet is full of it and its sub-optimal anyways

# Approach 2: Using priority queue, Time: O(n), Space: O(1)
# Very similar approach and intuition to:
# https://leetcode.com/problems/rearrange-string-k-distance-apart

# We need to arrange the characters in string such that each same character is K distance apart,
# where distance in this problems is time b/w two similar task execution.

# 1. Add tasks based on frequency to priority queue. We use negative values to get maxheap.
# 2. Pick the task in each round of 'n' with highest frequency. (heappop)
# 3. As you pick the task, decrease the frequency, and put them back after the round.


# Time: O(n), Actually it is: O(Nlog(N) * n) where N is the number of tasks and n is the cool-off period.
#       N <= 26 so we have O(Nlog(N) * n) => O(26log(26) * n) => O(n)
# Space: O(1), will not be more than O(26).
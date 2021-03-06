from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort(); heaters.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]    # add 2 fake heaters
        result, i = 0, 0

        for house in houses:
            while house > heaters[i + 1]: i += 1                # search to put house between heaters

            dis = min(house - heaters[i], heaters[i + 1] - house)
            result = max(result, dis)

        return result


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        result = float('-inf')

        for h in houses:
            index = self.bin_search(heaters, h)
            l_dist = h - heaters[index - 1] if index > 0 else float('inf')
            r_dist = heaters[index] - h if index < len(heaters) else float('inf')
            result = max(result, min(l_dist, r_dist))

        return result

    def bin_search(self, nums, target):
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] < target: l = mid + 1
            else:                  r = mid

        return l

# 475. Heaters
# https://leetcode.com/problems/heaters/description/


# public class Solution {
#     public int findRadius(int[] houses, int[] heaters) {
#         Arrays.sort(heaters);
#         int result = Integer.MIN_VALUE;
#         for (int house : houses) {
#             int index = Arrays.binarySearch(heaters, house);
#             if (index < 0) {
#               index = -(index + 1);
#             }
#             int dist1 = index - 1 >= 0 ? house - heaters[index - 1] : Integer.MAX_VALUE;
#             int dist2 = index < heaters.length ? heaters[index] - house : Integer.MAX_VALUE;

#             result = Math.max(result, Math.min(dist1, dist2));
#         }

#         return result;
#     }
# }

# The idea is to leverage decent Arrays.binarySearch() function provided by Java.

# For each house, find its position between those heaters (thus we need the heaters array to be sorted).
# Calculate the distances between this house and left heater and right heater, get a MIN value of those two values. Corner cases are there is no left or right heater.
# Get MAX value among distances in step 2. It's the answer.
# Time complexity: max(O(nlogn), O(mlogn)) - m is the length of houses, n is the length of heaters.

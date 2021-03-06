from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]    # add 2 fake heaters
        ans, i = 0, 0
        for house in houses:
            while house > heaters[i + 1]:                       # search to put house between heaters
                i += 1
            dis = min(house - heaters[i], heaters[i + 1] - house)
            ans = max(ans, dis)
        return ans


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

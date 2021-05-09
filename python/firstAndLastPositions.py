# firstAndLastPositions.py
# william pulkownik

# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# Follow up: Could you write an algorithm with O(log n) runtime complexity?

from bisect import bisect_left, bisect

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        #create a list variable to store the values
        locations = [-1,-1]
        leftTarget = bisect_left(nums, target)
        if leftTarget == len(nums) or nums[leftTarget] != target:
            return locations

        return [leftTarget, bisect(nums, target)-1]

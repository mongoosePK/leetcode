# furthestBuildingYouCanReach.py
# William Pulkownik
# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

# While moving from building i to building i+1 (0-indexed),

# If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
# If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
#

class Solution:
    def furthestBuilding(self, heights: [int], bricks: int, ladders: int) -> int:
        jump_heights = [heights[i + 1] - heights[i] for i in range(len(heights)-1)]
        jumpPostitions = enumerate(jump_heights)
        highestJumps = sorted(jumpPostitions, key=lambda x:x[1], reverse=True)
        ladderJumps = []
        skip = 0
        for i in range(ladders):
            while ladders > 0:
                ladderJumps.append(highestJumps[i])
                ladders -= 1
                
        
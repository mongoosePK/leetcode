# shuffleArray.py
# author: William Pulkownik
# this program taakes an integer array of numbers, *randomly* shuffles it, and resets it

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

from random import sample

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        count = len(self.nums)
        
        # Generate a random index list in the range of 0 to the nums count
        random_list = random.sample(self.nums, len(self.nums))
        return random_list


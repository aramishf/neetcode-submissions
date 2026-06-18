class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        # enumerate to get us i the index and n the number
        for i, n in enumerate(nums):
            complement = target - n

            if complement in map:
                return [ map[complement], i ] 
            
            map[n] = i;

        
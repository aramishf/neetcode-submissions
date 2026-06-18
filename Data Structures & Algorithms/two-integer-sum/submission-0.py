class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty hash map
        num_map = {}

        # Loop through the list
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is already in the map
            if complement in num_map:
                # If found, return the indices
                return [num_map[complement], i]
            
            # If not found, add the current number and its index to the map
            num_map[num] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (target == nums[i] + nums[j]):
                    return [i,j] 
        """
        # create empty set of unique elements called seen
        # store whatever we iterate through
        seen = {}

        for i, num in enumerate(nums):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]
                break
            
            seen[num] = i
        


            



        
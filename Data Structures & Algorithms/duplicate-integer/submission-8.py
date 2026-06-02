# 1,2,3,3
# 1 = 2 no
# 2 = 3 no
# 3 = 3 yes
# is duplicate = True
# return false
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        for n in range(len(nums) - 1):
            if (nums[n] == nums[n+1]):
                return True
        
        return False
        """

        if len(nums) == len(set(nums)):
            return False
        return True 


        

        
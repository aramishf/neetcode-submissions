class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #for i in range(len(nums)):
            #for j in range(i + 1,len(nums)):
                #if nums[i] == nums[j]:
                    #return True

        #return False

        # can use dictionary or hash map/set
        # go through nums and look at the first elem and put in dict
        # go through the next, and put it in dict and do comparison if found in dict
        # until found duplicate return True, otherwise False and keep comparing
        # until the end of nums

        duplicate = set()

        for number in nums:
            if number in duplicate:
                return True
            
            duplicate.add(number)
        
        return False



        
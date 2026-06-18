class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for i in range(len(nums)):
            #for j in range(i+ 1,len(nums)):
                #if target == nums[i] + nums[j]:
                    #return [i,j]
                
        #return [i,j]

        map = {} # value -> index

        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in map:
                return [map[diff], i]

            map[n] = i



        
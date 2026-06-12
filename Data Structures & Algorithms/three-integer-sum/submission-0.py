class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first + second + third = 0
        # second + third = 0 - first

        # [-4,-1,-1,0,1,2]
        #  f.  l.       r.
        nums.sort()
        results = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            first = -nums[i]

            while (l < r):
                curr_sum = nums[l] + nums[r]

                if curr_sum < first:
                    l += 1
                
                elif curr_sum > first:
                    r -= 1

                else:
                    results.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return results
        

        

        

    

        



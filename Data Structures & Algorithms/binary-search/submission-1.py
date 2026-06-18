class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2

            # check left side and right side
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
                
            else:
                # if target = mid then stop and return mid
                return mid
        
        return -1

            





                






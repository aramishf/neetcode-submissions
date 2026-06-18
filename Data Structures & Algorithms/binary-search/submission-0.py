class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid # found the target

            if target > nums[mid]:
                l = mid + 1 # target in right half, move left pointer up
            else:
                r = mid - 1

        return -1 # if not found 


        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        sum = 0

        # keep l at start, r at the end
        while (l < r):
            sum = numbers[l] + numbers[r]

            if (sum == target):
                return [l+1,r+1]
            
            elif (sum > target):
                r = r-1
            
            elif (sum < target):
                l = l + 1

        
        # 0 < 3
        # sum = 5
        # 5 == 3 nope
        # 5 > 3 yes -> 2
        # 0 < 2
        # sum = 1 + 3 = 4 
        # 4 == 3 nope
        # 4 > 3 yhes
        # r=1
        # 0 < 1 
        # sum = 3
        # 3 == 3 yes
        return 
            
        
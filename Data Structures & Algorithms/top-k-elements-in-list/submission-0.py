class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # track each char counts in nums
        # then k tells us the most freq elements in nums
        # return those k freq elements 

        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        arr = []    
        for num, freq in count.items():
            arr.append([freq, num])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

    

            

        """ count = {1:1 
                     2:2
                     3:3}

        k = 2

        lets suppose count dict is sorted 
        



        """
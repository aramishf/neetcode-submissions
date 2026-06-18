class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # track each char counts in nums
        # then k tells us the most freq elements in nums
        # return those k freq elements 


        count = {}

        for number in nums:
            if number in count:
                count[number] += 1 
            else:
                count[number] = 1

        
        """ count = {1:1, 2:2, 3:3}
        """

        arr = []

        for number, freq in count.items():
            arr.append((freq, number))

        arr.sort(reverse=True)


        # arr = [(3,3), (2:2), (1,1)]

        i = 0
        res = []

        while (i < k):
            # check for the highest k numbers
            # return numbers in list
            res.append(arr[i][1])
            i += 1

        return res


        


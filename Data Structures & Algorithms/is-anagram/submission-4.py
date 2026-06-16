class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # two hashmap for strings
        # key (char), value (count)
        # s[r] = 2

        # racecar and carrace
        # have same charcter counts and len

        if len(s) != len(t):
            return False

        count_char_s = {}
        count_char_t = {}

        # check if char in s in map, then +1 
        # if not seen in map then add count to 1
        # count_char_s[c] = count 
        
        for char in s:
            if char in count_char_s:
                count_char_s[char] += 1
            else:
                count_char_s[char] = 1

        for char in t:
            if char in count_char_t:
                count_char_t[char] += 1
            else:
                count_char_t[char] = 1

        return count_char_s == count_char_t 



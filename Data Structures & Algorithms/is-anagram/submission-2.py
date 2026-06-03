class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two strings if they are anagram
        # then have exact same characters 
  
        if len(s) != len(t):
            return False
        
        # go through each char in s string, append on stack, 
        # then each char in t , if found on stack then remove
        # if stack is empty then return True
        stack = []

        for char in range(len(s)):
            stack.append(s[char])
        
        for c in range(len(t)): 
            if t[c] in stack:
                stack.remove(t[c])

        if not stack:
            return True

        return False


            
            
        

            
            
        
            

        
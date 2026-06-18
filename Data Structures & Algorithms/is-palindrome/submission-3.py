class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Initialize pointers
        l, r = 0, len(s) - 1

        while l < r:
            # 2. Move left pointer if current char is not alphanumeric
            while l < r and not s[l].isalnum():
                l += 1
            
            # 3. Move right pointer if current char is not alphanumeric
            while l < r and not s[r].isalnum():
                r -= 1
            
            # 4. Compare (converting to lower case)
            if s[l].lower() != s[r].lower():
                return False
            
            # 5. Move both pointers inward
            l += 1
            r -= 1
            
        return True
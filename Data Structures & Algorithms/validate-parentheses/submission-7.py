class Solution:
    def isValid(self, s: str) -> bool:
        #valid = '(){}[]'

        #for char in range(len(s)):
            #if s[char] in valid:
                #return True
        
        #return False

        # stack is last in - first out
        # when see open bracket push on stack
        # as you see closed bracket , pop out of stack
        # return False if pop a closing bracket but no opening bracket in stack
        close_to_open_map = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for ch in s:
            if ch in close_to_open_map:
                if stack and stack[-1] == close_to_open_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False






        

        
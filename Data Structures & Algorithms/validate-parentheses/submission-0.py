class Solution:
    def isValid(self, s: str) -> bool:

        # check if string is an even number before
        #if len(s) % 2 != 0:
            #return False

        # Keep looping until find pair exists in string
        #while "()" in s or "{}" in s or '[]' in s:
            #s = s.replace("()", "")  
            #s = s.replace("{}", "")  
            #s = s.replace("[]", "")     

        # if the string is empty then it was true and valid string
        #return s == ""   

        ### using STACKS
        stack = []
        
        # map - key is closer, value is opener
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in closeToOpen:
                # if stack isnt empty and top matches 
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                #It's an opener, add to stack
                stack.append(c)
        
        #True only if every opener was matched (stack is empty)
        return True if not stack else False
    
        
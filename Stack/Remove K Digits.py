class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for c in num:
            while k>0 and stack and stack[-1]>c:
                k-=1
                stack.pop()
            stack.append(c)
        stack=stack[:len(stack)-k]
        # Join the stack and remove leading zeros
        res = ''.join(stack).lstrip('0')
        
        # Return the result or '0' if empty
        return res if res else '0'
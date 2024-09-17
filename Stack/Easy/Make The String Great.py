class Solution:
    def makeGood(self, s: str) -> str:
        def lower(c):
            if ord(c)<ord('a'):
                return chr(ord('a')+ord(c)-ord('A'))
            return c
        
        stack=[]
        i=0
        while i<len(s):
            if (stack and stack[-1]!=s[i] and lower(stack[-1])==lower(s[i])):
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
        return "".join(stack)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=0
        stack=[]
        for p in pushed:
            stack.append(p)
            while stack and stack[-1]==popped[i]:
                stack.pop()
                i+=1
        return len(stack)==0
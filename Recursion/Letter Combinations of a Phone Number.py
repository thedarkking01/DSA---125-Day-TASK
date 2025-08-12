class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res=[]
        def backtrack(index:int,current:str):
            if index==len(digits):
                res.append(current)
                return 
            for char in phone_map[digits[index]]:
                backtrack(index+1,current+char)
        backtrack(0,"")
        return res
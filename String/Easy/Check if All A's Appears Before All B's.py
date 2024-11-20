class Solution:
    def checkString(self, s: str) -> bool:
        # for i in range(len(s)):
        #     if s[i]=='b':
        #         if 'a' in s[i+1:]:
        #             return False
        #         return True
        #     elif 'b' not in s:
        #         return True
        return 'ba' not in s

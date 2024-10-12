class Solution:
    def reverseWords(self, s: str) -> str:
        word=s.split()
        rev=word[::-1]
        revstr=" ".join(rev)
        return revstr
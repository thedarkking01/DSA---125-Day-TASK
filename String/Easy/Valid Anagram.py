class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts,countt={},{}
        for i in range(len(s)):
            counts[s[i]]=1+counts.get(s[i],0)
            countt[t[i]]=1+countt.get(t[i],0)
        return countt==counts
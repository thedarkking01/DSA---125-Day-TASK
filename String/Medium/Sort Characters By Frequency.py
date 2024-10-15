class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        bucket=defaultdict(list)
        for c,cnt in count.items():
            bucket[cnt].append(c)
        res=[]
        for i in range(len(s),0,-1):
            for c in bucket[i]:
                res.append(c*i)
        return "".join(res)
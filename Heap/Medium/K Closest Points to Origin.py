class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for x,y in points:
            dis=x**2+y**2
            minheap.append([dis,x,y])
        
        heapq.heapify(minheap)
        res=[]
        while k>0:
            dis,x,y=heapq.heappop(minheap)
            res.append((x,y))
            k-=1
        return res
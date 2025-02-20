class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)
            
        q = deque([(headID, 0)])  # (id, time)
        res = 0
        
        while q:
            node, time = q.popleft()
            res = max(res, time)
            for emp in adj[node]:
                q.append((emp, time + informTime[node]))
        
        return res
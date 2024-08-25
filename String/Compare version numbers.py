class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split('.')
        v2=version2.split('.')
        N1=len(v1)
        N2=len(v2)
        for i in range(max(N1,N2)):
            n1=int(v1[i]) if i<N1 else 0
            n2=int(v2[i]) if i<N2 else 0
            if n1<n2:
                return -1
            elif n1>n2:
                return 1
        return 0
#code link = https://www.naukri.com/code360/problems/1062679?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTabValue=PROBLEM
# platform - Coding ninja
def NthRoot(n: int, m: int) -> int:
    l,r=1,m
    while l<r:
        mid=(l+r)//2
        if mid**n==m:
            return mid
        if mid**n<m:
            l=mid+1
        else:
            r=mid-1
    return -1
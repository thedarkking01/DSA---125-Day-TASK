class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        for i in range(1,numRows):
            tmp=[0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1]) + 1):
                row.append(tmp[j] + tmp[j+1])
            res.append(row)
        return res
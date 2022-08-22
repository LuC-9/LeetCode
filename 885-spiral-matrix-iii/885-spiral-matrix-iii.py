class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        #            E       S      W      N
        dir_idx=0
        tot=rows*cols
        steps=1
        inc=1
        res=[[rStart,cStart]]
        while(len(res)<tot):
            for i in range (inc):
                rStart,cStart=rStart+directions[dir_idx][0],cStart+directions[dir_idx][1]
                if rStart>=0 and rStart<rows and cStart >= 0 and cStart < cols:
                    res.append([rStart,cStart])
            dir_idx=(dir_idx+1)%4
            if steps % 2 ==0:
                inc+=1
            steps+=1
        return res
        
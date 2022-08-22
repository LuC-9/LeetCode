class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        #East,South,West,North
        dir_idx=0
        steps=1
        inc=1
        res=[[rStart,cStart]]
        while(len(res)<rows*cols):
            for i in range(inc):
                rStart,cStart=rStart+directions[dir_idx][0],cStart+directions[dir_idx][1]
                # increase according to directions 
                
                # if it goes out of matrix discard or else append in result
                if rStart>=0 and rStart<rows and cStart>=0 and cStart<cols:
                    
                    res.append([rStart,cStart])
            dir_idx=(dir_idx+1)%4
            # change the direction after suitable steps
            
            # if current steps(steps) are even increment the inc(i.e steps to be taken)
            if steps%2==0:
                inc+=1
            steps+=1
            """
            
            we can avoid use of variable step by using below snippet in it's place
            inc += not(dir_idx%2), i.e. add 1 if dir_idx is even or 0
            
            """
            
        return res
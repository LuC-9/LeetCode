class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        st=""
        arr=[]
        for i in num:
            st+=str(i)
        st=int(st)+k
        st=str(st)
        for i in st:
            arr.append(i)
        return arr
        
        
        
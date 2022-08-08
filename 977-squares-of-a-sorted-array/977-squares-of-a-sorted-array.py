class Solution:
    def sortedSquares(self, array: List[int]) -> List[int]:
        arr=[0 for i in array] 
        i=len(array)-1
        start=0 # start pointer at 0 index
        end=len(array)-1 # wnd pointer at last index
        while start<=end:
            smaller=array[start]
            larger = array[end]
            if abs(smaller)>=abs(larger):
                arr[i]=smaller**2
                start+=1
            if abs(smaller)<abs(larger):
                arr[i]=larger**2
                end-=1
            i-=1
        return arr
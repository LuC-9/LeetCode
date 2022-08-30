class Solution:
    def threeSum(self, array: List[int]) -> List[List[int]]:
        targetSum=0
        li=set()
        array.sort()
        cur=0
        while cur < len(array)-2:
            l=cur+1
            r=len(array)-1 
            while l<r:
                if array[cur]+array[l]+array[r]==targetSum:
                    li.add((array[cur],array[l],array[r]))
                    l+=1
                    r-=1
                elif array[cur]+array[l]+array[r]<targetSum:
                    l+=1
                elif array[cur]+array[l]+array[r]>targetSum:
                    r-=1
            cur+=1
        return li
        
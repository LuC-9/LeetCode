class Solution:
    def threeSum(self, array: List[int]) -> List[List[int]]:
        t=0
        li=set()
        array.sort()
        cur=0
        while cur < len(array)-2:
            l=cur+1
            r=len(array)-1 
            while l<r:
                if array[cur]+array[l]+array[r]==t:
                    li.add((array[cur],array[l],array[r]))
                    l+=1
                    r-=1
                elif array[cur]+array[l]+array[r]<t:
                    l+=1
                elif array[cur]+array[l]+array[r]>t:
                    r-=1
            cur+=1
        return list(li)
        
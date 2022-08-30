class Solution:
    def threeSum(self, array: List[int]) -> List[List[int]]:
        targetSum=0
        li=set()
        array.sort()
        cur=0
    #print(array)
    #print(right)
        while cur < len(array)-2:
            left=cur+1
            right=len(array)-1 
            while left<right:
                if array[cur]+array[left]+array[right]==targetSum:
                    li.add((array[cur],array[left],array[right]))
                    left+=1
                    right-=1
                elif array[cur]+array[left]+array[right]<targetSum:
                    left+=1
                elif array[cur]+array[left]+array[right]>targetSum:
                    right-=1
            cur+=1
        return list(li)
        
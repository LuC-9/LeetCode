class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l=[str(x) for x in nums]
        c=0
        for i in l:
            if(len(i)&1):
                c+=1
        return len(l)-c   
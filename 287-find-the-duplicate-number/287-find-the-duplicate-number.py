class Solution:
    def findDuplicate(self, array: List[int]) -> int:
        for i in array:
            ab=abs(i)
            if array[ab-1]<0:
                return ab
            array[ab-1]*=-1
        return -1
        
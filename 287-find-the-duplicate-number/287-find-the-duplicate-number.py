class Solution:
    def findDuplicate(self, array: List[int]) -> int:
        for i in array:
            absi=abs(i)
            # if the mapped index value is already negative
            if array[absi%len(array)]<0:
                return absi
            #make the mapped value negative(a value is mapped to index element%len(array)
            array[absi%len(array)]*=-1
        return -1
        
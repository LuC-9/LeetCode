class Solution:
    def removeElement(self,array: List[int], val: int) -> int:
        i = 0
        for index in range(len(array)):
            
            if array[index] != val:
                array[index], array[i] = array[i], array[index]
                i += 1
        return i
        
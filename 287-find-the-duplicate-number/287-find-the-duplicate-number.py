class Solution:
    def findDuplicate(self, array: List[int]) -> int:
        seen=set()
        for i in array:
            if i in seen:
                return i
            else:
                seen.add(i)
        return -1
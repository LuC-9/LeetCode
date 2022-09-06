class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        k=0
        for i in operations:
            if i[1]=="-":
                k-=1
            if i[1]=="+":
                k+=1
        return k
                
        
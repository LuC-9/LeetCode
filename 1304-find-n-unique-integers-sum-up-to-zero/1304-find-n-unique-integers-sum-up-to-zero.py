class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(-(n//2), 0)) + [0]*(n % 2) + list(range(1, n//2 + 1))
        
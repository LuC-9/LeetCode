class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k=1
        for i in range(len(digits) - 1, -1, -1):
            if not k: break
            k, digits[i] = divmod(digits[i] + k, 10)
        while k:
            k, a = divmod(k, 10)
            digits = [a] + digits
        return digits 
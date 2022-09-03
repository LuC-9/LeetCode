class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(10))
        queue = deque(list(range(1, 10)))
        for n in range(N - 1):
            len_queue = len(queue)
            for j in range(len_queue):
                num = queue.popleft()
                lsd = num % 10
                if lsd - K >= 0:
                    queue.append( num * 10 + lsd - K )
                if K and lsd + K <= 9:
                    queue.append( num * 10 + lsd + K )
        return list(queue)
        
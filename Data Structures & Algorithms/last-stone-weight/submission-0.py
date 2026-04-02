class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)

            if first > second:
                heapq.heappush(stones, -1 * (first-second))
                
        stones.append(0)
        return abs(stones[0])
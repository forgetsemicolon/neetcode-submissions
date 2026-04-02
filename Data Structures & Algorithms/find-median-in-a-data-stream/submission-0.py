class MedianFinder:

    def __init__(self):
        # two heaps - 
        # small - max heap
        # large - min heap
        # heaps should be equal size 
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # maxHeap and hence multiply by -1
        heapq.heappush(self.small, -1 * num)

        # make sure every num in small <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            # pop the value from maxHeap and multiple by -1
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size of heaps (diff in size more than 1)
        # large heap is larger
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) < len(self.large):
            return self.large[0]
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        return (-1 * self.small[0] + self.large[0]) / 2
        
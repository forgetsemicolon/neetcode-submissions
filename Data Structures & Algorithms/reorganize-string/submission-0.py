class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ''
        freq = Counter(s)
        maxHeap = [(-count, char) for char, count in freq.items()]

        heapq.heapify(maxHeap)

        prev = None
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            res += char
            
            if prev:
                heapq.heappush(maxHeap, prev)
                
            count += 1
            if count < 0:
                prev = (count, char)
            else:
                prev = None

        return res if len(res) == len(s) else ""
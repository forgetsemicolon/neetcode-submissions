class FreqStack:

    def __init__(self):
        self.heap = []
        self.cnt = defaultdict(int)
        self.index = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        heapq.heappush(self.heap, (-self.cnt[val], -self.index, val))

        self.index += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.cnt[val] -= 1
        return val

    # def __init__(self):
    #     self.stack = []

    # def push(self, val: int) -> None:
    #     existing = [freq for v, freq in self.stack if v == val]
    #     if not existing:
    #         self.stack.append((val, 1))
    #     else:
    #         self.stack.append((val, max(existing) + 1))

    # def pop(self) -> int:
    #     maxFreq = max(freq for _, freq in self.stack)

    #     for i in range(len(self.stack)-1, -1, -1):
    #         if self.stack[i][1] == maxFreq:
    #             val = self.stack[i][0]
    #             self.stack.pop(i)
    #             return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
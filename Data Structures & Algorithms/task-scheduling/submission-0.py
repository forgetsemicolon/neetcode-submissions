class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a maxHeap for the counts of tasks
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                # reduce by 1 since we are using the task now
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt:
                    q.append([cnt, time+n])

            # if we have reached the time when a particular 
            # task can be added by to the maxHeap again,
            # we remove it from the queue and add it to maxheap
            if q and q[0][1] == time:
                # we just want the count and not the time 
                # which is [1] element 
                ele = q.popleft()[0]
                heapq.heappush(maxHeap, ele)

        return time 
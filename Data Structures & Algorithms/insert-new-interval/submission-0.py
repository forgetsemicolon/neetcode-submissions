class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)
        i = 0

        # while i<n and intervals[i][0] > newInterval[1]:
        #     result.append(newInterval)
        #     i += 1

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        while i<n:
            result.append(intervals[i])
            i += 1

        return result

        # cumulativeInterval = []
        # for i in range(1,len(intervals)):
        #     if intervals[i][0] > newInterval[0]:
        #         cumulativeInterval[i][0] = intervals[i-1][0]
        #     else:
        #         cumulativeInterval[i][0] = intervals[i][0]

        # for i in range(1,len(intervals)):
        #     if intervals[i][1] < newInterval[1]:
        #         cumulativeInterval[i][1] = newInterval[1]
        #     else:
        #         cumulativeInterval[i][0] = intervals[i][0]
                
        # return cumulativeInterval
            
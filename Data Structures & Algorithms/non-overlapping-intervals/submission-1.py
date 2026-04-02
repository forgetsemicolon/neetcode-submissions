class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        i = 1

        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        while i < n:
            if intervals[i][0] < prev_end:
                count += 1
            
            else:
                prev_end = intervals[i][1]

            i += 1

        return count
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        n = len(intervals)

        res = [intervals[0]]

        i = 1

        while i < n:
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])


            else:
                res.append(intervals[i])

            i += 1

        return res
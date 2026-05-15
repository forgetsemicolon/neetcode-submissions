class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # the min of binary search is the max(weights)
        # and then from there we start and go until sum(weights)
        # so between max(weights) to sum(weights) is our answer
        # for each value in that range we check what is the number
        # of days and return the min value in the range for which 
        # number of days is <= days

        l = max(weights)
        r = sum(weights)

        minWeight = r

        def getDays(val):
            days = 1
            curr_sum = 0
            
            for w in weights:
                if curr_sum + w > val:
                    days += 1
                    curr_sum = 0

                curr_sum += w

            return days 

        # for val in range(l,r+1):
        #     x = getDays(val)

        #     if x <= days and val < minWeight:
        #         minWeight = val

        while l < r:
            m = (l+r) // 2

            if getDays(m) > days:
                l = m+1
            else:
                r = m

        return l



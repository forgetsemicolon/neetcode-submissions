class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(n) solution 
        res = []
        q = collections.deque() # stores elements
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window as window is sliding
            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1

        return res
        
        # O(n) solution (but doesn't work)
        # res = []

        # l = 0
        # r = l + k - 1

        # res.append(max(nums[l:r+1]))

        # while r < len(nums)-1:
        #     l += 1
        #     r += 1

        #     res.append(max(res[-1], nums[r]))

        # return res

        # # following solution was timeout for large k
        # # time complexity - O(k.(n-k))
        # res = []

        # l = 0
        # r = l + k - 1

        # while r < len(nums):
        #     res.append(max(nums[l:r+1]))
        #     l += 1
        #     r += 1

        # return res
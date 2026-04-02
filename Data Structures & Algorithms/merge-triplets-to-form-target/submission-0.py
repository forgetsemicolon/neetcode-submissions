class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for t in triplets:
            if (t[0]>target[0] or t[1]>target[1] or t[2]>target[2]):
                triplets.remove(t)

        flag_a = flag_b = flag_c = False
        for (a,b,c) in triplets:
            if a == target[0]:
                flag_a = True
            if b == target[1]:
                flag_b = True
            if c == target[2]:
                flag_c = True

        return (flag_a and flag_b and flag_c)
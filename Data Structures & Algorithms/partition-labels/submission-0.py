class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i in range(len(s)):
            d[s[i]] = i

        start = farthest = 0
        res = []

        for i in range(len(s)):
            farthest = max(farthest, d[s[i]])

            if i == farthest:
                res.append(farthest-start+1)

                start = farthest + 1


        return res

            
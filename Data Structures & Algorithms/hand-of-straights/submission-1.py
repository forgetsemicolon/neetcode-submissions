class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        d = {}
        for h in hand:
            d[h] = d.get(h,0) + 1

        sorted_keys = sorted(d.keys())

        for num in sorted_keys:
            count = d[num]

            if count == 0:
                continue

            for i in range(groupSize):
                next_card = num + i

                if next_card not in d or d[next_card] < count:
                    return False

                d[next_card] -= count

        return True

        
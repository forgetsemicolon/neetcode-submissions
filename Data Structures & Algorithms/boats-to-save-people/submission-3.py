class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0

        people.sort()

        l, r = 0, len(people)-1

        while l < r:
            if people[l] == limit:
                people[l] = 0
                boat += 1
                l += 1
                continue

            if people[r] == limit:
                people[r] = 0
                boat += 1
                r -= 1
                continue

            w = people[l] + people[r]

            if w <= limit:
                people[l] = people[r] = 0
                boat += 1
                l += 1
                r -= 1

            else:
                r -= 1

        for p in people:
            if p != 0:
                boat += 1

        return boat

        

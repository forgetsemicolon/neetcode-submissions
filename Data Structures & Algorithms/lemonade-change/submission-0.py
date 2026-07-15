class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        FIVES = 0
        TENS = 0
        res = False

        for i in range(len(bills)):
            if bills[i] == 5:
                FIVES += 1
                continue

            elif bills[i] ==10:
                TENS += 1
                if FIVES > 0:
                    FIVES -= 1
                    continue
                
                else:
                    return False

            else:
                if TENS > 0 and FIVES > 0:
                    TENS -= 1
                    FIVES -= 1

                elif FIVES >= 3:
                    FIVES -= 3

                else:
                    return False

        return True     
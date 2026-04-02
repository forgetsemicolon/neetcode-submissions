class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def helper(amount, coin_index):
            if amount == 0:
                return 1

            if coin_index < 0:
                return 0

            if amount < 0:
                return 0

            if (amount, coin_index) in dp:
                return dp[(amount, coin_index)]

            ways = 0
            ways += helper(amount - coins[coin_index], coin_index)
            ways += helper(amount, coin_index-1)

            dp[(amount,coin_index)] = ways

            return dp[(amount, coin_index)]

        return helper(amount, len(coins) - 1)
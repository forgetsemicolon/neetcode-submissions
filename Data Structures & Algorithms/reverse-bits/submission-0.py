class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1 # shift by i and mask with 1 to get the last bit
            res += (bit << (31-i)) # add the bit to the reveresed position 

        return res
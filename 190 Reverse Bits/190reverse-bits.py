class Solution:
    def reverseBits(self, n: int) -> int:
        bina=format(n,'032b')
        bi=bina[::-1]
        return int(bi,2)
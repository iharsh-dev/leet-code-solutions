class Solution:
    def flip(self, b: str)-> str:
        trans=str.maketrans("01","10")
        return b.translate(trans)

    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(1,n):
            d=self.flip(s)
            s=s+"1"+d[::-1]
        return s[k-1]
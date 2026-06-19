class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        new = start^goal 
        strr = bin(new)[2:]
        arr = [int(x) for x in strr]
        return sum(arr)
        
            
        
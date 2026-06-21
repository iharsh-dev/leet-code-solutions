class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = len(costs)
        curr = 0 
        for i in range(n):
            curr+=costs[i]
            if curr > coins:
                return i 
        return n
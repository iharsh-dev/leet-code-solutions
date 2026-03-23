class Solution:
    def minC(self, cost: List[int], n:int,memo) -> int:
        if n>=len(cost):
            return 0
        else:
            if n in memo:
                return memo[n]
            else:
                memo[n]=min(self.minC(cost,n+1,memo)+cost[n],self.minC(cost,n+2,memo)+cost[n])
                return memo[n]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        return min(self.minC(cost,1,memo),self.minC(cost,0,memo))
          
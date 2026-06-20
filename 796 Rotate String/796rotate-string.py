class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        num = s+s
        if len(goal) == len(s) and goal in num:
            return True
        else:
            return False
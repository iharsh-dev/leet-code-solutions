class Solution:
    def judgeCircle(self, moves: str) -> bool:
        L = moves.count('L')
        R = moves.count('R')
        U = moves.count('U')
        D = moves.count('D')
        if L == R and U == D:
            return True
        else:
            return False
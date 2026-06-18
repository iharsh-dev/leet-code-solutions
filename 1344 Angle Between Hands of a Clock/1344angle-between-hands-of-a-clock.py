class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(30*hour - 5.5*minutes)
        if angle > 180 :
            return 360 - angle 
        return angle

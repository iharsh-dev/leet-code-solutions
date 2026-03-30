class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s_1_even=list(s1[::2])
        s_1_even.sort()
        s_1_odd=list(s1[1::2])
        s_1_odd.sort()
        s_2_even=list(s2[::2])
        s_2_even.sort()
        s_2_odd=list(s2[1::2])
        s_2_odd.sort()
        if s_1_even==s_2_even and s_1_odd==s_2_odd:
            return True
        else:
            return False

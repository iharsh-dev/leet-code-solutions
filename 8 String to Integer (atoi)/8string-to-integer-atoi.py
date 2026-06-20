class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        check = True
        c = 1
        for i in s:
            if check and (i == '_' or i == ' ') :
                m = 0 
            elif i == '+' and check:
                check = False
                c = 1
            elif i == '-' and check:
                check = False
                c = -1
            elif 0 <= ord(i)-48 <= 9:
                check = False
                ans*=10
                ans+=(ord(i)-48)
            else:
                break 
        if c*ans < -2147483648:
            return -2147483648 
        elif c*ans > 2147483647:
            return 2147483647
        else:
            return c*ans

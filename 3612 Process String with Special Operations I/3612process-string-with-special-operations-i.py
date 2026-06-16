class Solution:
    def processStr(self, s: str) -> str:
        a = ""
        for i in s:
            if i == '*':
                a = a[:-1] 
            elif i == '#' :
                a = a + a 
            elif i == '%' :
                a = a[::-1]
            else:
                a += i
        return a
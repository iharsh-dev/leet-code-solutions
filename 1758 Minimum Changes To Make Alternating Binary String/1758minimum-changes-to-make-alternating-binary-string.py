class Solution:
    def minOperations(self, s: str) -> int:
        num_1=0
        num_2=0
        for i in range(len(s)):
            if i%2==0:
                if s[i]!='0':
                    num_1+=1
            else:
                if s[i]!='1':
                    num_1+=1
        for i in range(len(s)):
            if i%2==0:
                if s[i]!='1':
                    num_2+=1
            else:
                if s[i]!='0':
                    num_2+=1
        return min(num_1,num_2)
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(num1,num2+1):
            dig = [ int(j) for j in str(i)]
            for k in range(1,len(dig)-1):
                if dig[k] > dig[k-1] and dig[k] > dig[k+1]:
                    count+=1
                elif dig[k] < dig[k-1] and dig[k] < dig[k+1]:
                    count+=1 
        return count
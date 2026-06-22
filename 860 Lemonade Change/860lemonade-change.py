class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dicti ={20:0,10:0,5:0}
        for i in bills:
            dicti[i]+=1
            change = (i-5)
            while change > 0:
                if change >= 10:
                    if dicti[10] > 0:
                        change-=10
                        dicti[10]-=1
                    elif dicti[5] > 0:
                        change-=5
                        dicti[5]-=1 
                    else:
                        return False
                else:
                    if dicti[5] > 0:
                        change-=5
                        dicti[5]-=1 
                    else:
                        return False
        return True
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        ret=[]
        s=[int(i) for i in digits]
        for i in range(len(mapp[s[0]-2])):
            ans=mapp[s[0]-2][i]
            if len(s)>1:
                for j in range(len(mapp[s[1]-2])):
                    ans+=mapp[s[1]-2][j]
                    if len(s)>2:
                        for k in range(len(mapp[s[2]-2])):
                            ans+=mapp[s[2]-2][k]
                            if len(s)>3:
                                for l in range(len(mapp[s[3]-2])):
                                    ans+=mapp[s[3]-2][l]
                                    ret.append(ans)
                                    ans=ans[:-1]
                                ans=ans[:-1]
                            else:
                                ret.append(ans)
                                ans=ans[:-1]
                        ans=ans[:-1]
                    else:
                        ret.append(ans)
                        ans=ans[:-1]
                ans=ans[:-1]
            else:
                ret.append(ans)
                ans=ans[:-1]
        ans=ans[:-1]
        return ret   

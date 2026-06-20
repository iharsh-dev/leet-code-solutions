class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minn = len(strs[0])
        for i in strs:
            if len(i) < minn:
                minn = len(i)
        ans = ""
        for i in range(minn):
            check = True 
            curr = strs[0][i]
            for j in strs:
                if j[i] != curr:
                    check = False
                    break 
            if check:
                ans+=curr
            else:
                break
        return ans
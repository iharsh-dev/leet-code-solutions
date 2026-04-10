class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mapa = defaultdict(list)
        keys = set(nums)
        ans = []
        for i in range(len(nums)):
            mapa[nums[i]].append(i)
        for i in keys:
            if len(mapa[i])>=3:
                mapa[i].sort()
                minn = float('inf')
                for j in range(len(mapa[i])-2):
                    dist = 0
                    for k in range(j,j+3):
                        for m in range(k+1,j+3):
                            dist += abs(mapa[i][k]-mapa[i][m])
                    if minn > dist :
                        minn = dist
                ans.append(minn)
        if len(ans) > 0:
            return min(ans)
        else:
            return -1
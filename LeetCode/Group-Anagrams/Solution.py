1class Solution:
2    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
3        mapa = defaultdict(list)
4
5        for i in strs:
6            arr = sorted(i)
7            brr = "".join(arr)
8            mapa[brr].append(i)
9        
10        res = []
11        for key in mapa:
12            res.append(mapa[key])
13        
14        return res
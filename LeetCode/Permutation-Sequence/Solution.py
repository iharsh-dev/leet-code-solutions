1from itertools import permutations
2class Solution:
3    def getPermutation(self, n: int, k: int) -> str:
4        arr = [i for i in range(1,n+1)]
5        perm = list(permutations(arr))
6
7        perm.sort()
8        return "".join([str(i) for i in perm[k-1]])
9
10
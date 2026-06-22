class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = "balloon"
        d2 = Counter(s)
        d1 = Counter(text)
        minn = 10**4
        for key in d2:
            curr = d1[key]//d2[key]
            minn = min(minn,curr)
        return minn
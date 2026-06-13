class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""
        for i in words:
            weight = 0
            for j in i:
                weight+=weights[ord(j)-97]
            weight = weight%26 
            ans += chr(122-weight)
        return ans
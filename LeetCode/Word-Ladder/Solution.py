1from collections import deque,defaultdict
2class Solution:
3    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
4        words = set(wordList)
5        if endWord not in words:
6            return 0
7        alpha = [chr(i) for i in range(97,123)]
8        queue = deque([(beginWord, 1)])
9
10        while queue:
11            word, level = queue.popleft()
12            if word == endWord:
13                return level
14            for i in range(len(word)):
15                    for letter in alpha:
16                        new = word[:i]+letter+word[i+1:]
17                        if new in words:
18                            words.remove(new)
19                            queue.append((new,level + 1))
20        
21        return 0
22
23                            
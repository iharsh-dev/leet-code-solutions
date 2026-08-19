1from collections import defaultdict
2class Solution:
3    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
4        seats = defaultdict(list)
5
6        for row, seat in reservedSeats:
7            seats[row].append(seat)
8        group = n * 2
9        for key in seats:
10            left = True
11            right = True
12            middle = True
13            for x in seats[key]:
14                if 2 <= x <= 9:
15                    if x < 4:
16                        left = False 
17                    elif x > 7:
18                        right = False
19                    else:
20                        middle = False
21                        if x <= 5:
22                            left = False
23                        else:
24                            right = False 
25            if not left:
26                if middle or right:
27                    group -=1
28                else:
29                    group -= 2
30            else:
31                if not right:
32                    group -= 1
33            
34            
35        return group
36
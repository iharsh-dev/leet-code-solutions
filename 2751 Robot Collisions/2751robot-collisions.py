class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        mapa = {a: [b,c] for a,b,c in zip(positions, healths, directions)}
        temp=positions[:]
        positions.sort()
        stack=[]
        pos=0
        while pos < n:
            if mapa[positions[pos]][1]=='R':
                stack.append(positions[pos])
                pos+=1
            else:
                while mapa[positions[pos]][0]>0 and len(stack)>0:
                    top = stack[-1]
                    if mapa[top][0] < mapa[positions[pos]][0]:
                        mapa[top][0]=0
                        stack.pop()
                        mapa[positions[pos]][0]-=1
                    elif mapa[top][0] == mapa[positions[pos]][0]:
                        mapa[top][0]=0
                        mapa[positions[pos]][0]=0
                        stack.pop()
                        break
                    else:
                        mapa[positions[pos]][0]=0
                        mapa[top][0]-=1
                        break
                pos+=1
        ans=[]
        for i in temp:
            if mapa[i][0]!=0:
                ans.append(mapa[i][0])
        return ans

                    

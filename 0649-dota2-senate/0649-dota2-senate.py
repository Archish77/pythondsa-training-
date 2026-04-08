from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dir = deque()
        n = len(senate)

        
        for i,s in enumerate(senate):
            if s == 'R':
                rad.append(i)
            else:
                dir.append(i)

       
        while rad and dir:
            r = rad.popleft()  
            d = dir.popleft()   

            if r < d:          
                rad.append(r + n)  
            else:               
                dir.append(d + n)  

        return "Radiant" if rad else "Dire"
class Solution:

    def __init__(self):
        self.symbol={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }

    def romanToInt(self, s: str) -> int:
        num=0
        i=len(s)-1
        isCounted=[False for i in range(len(s))]

        while i>=1:
            if self.symbol[ s[i-1] ] < self.symbol[ s[i] ]:
                num+= (self.symbol[s[i]] - self.symbol[s[i-1]])
                isCounted[i]=True
                isCounted[i-1]=True
                i-=2
            else:
                num+= self.symbol[s[i]]
                isCounted[i]=True
                i-=1            

        if isCounted[0]==False:    
            num+= self.symbol[s[0]]
        
        return num
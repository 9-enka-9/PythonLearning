class Solution(object):
    dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        while (i < len(s)):
            if (i == (len(s)-1)):
                num += self.dict[s[i]]
                i += 1
            elif (self.dict[s[i]]*5 == self.dict[s[i+1]]):
                num += self.dict[s[i+1]] - self.dict[s[i]]
                i += 2
            elif ((self.dict[s[i]]*10 == self.dict[s[i+1]])):
                num += self.dict[s[i+1]] - self.dict[s[i]]
                i += 2
            else:
                num += self.dict[s[i]]
                i += 1
        return num

        
        
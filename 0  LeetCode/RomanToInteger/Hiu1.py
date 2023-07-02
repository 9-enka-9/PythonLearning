class Solution(object):
    dict = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    def toInt(self, s):
        if (self.dict.get(s) != None):
            return self.dict.get(s)
        for i in range(len(s),-1,-1):
            if (self.dict.get(s[:i]) != None):
                return self.dict.get(s[:i])+self.toInt(s[i:])

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.toInt(s)
        
        
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
        while (i != len(s)):
            if (s[i] == 'I'):
                if (i != (len(s)-1)):
                    if (s[i+1] == 'V'):
                        num += 4
                        i += 1
                    elif (s[i+1] == 'X'):
                        num += 9
                        i += 1
                    else:
                        num += 1
                else:
                    num += 1
            elif (s[i] == 'X'):
                if (i != (len(s)-1)):
                    if (s[i+1] == 'L'):
                        num += 40
                        i += 1
                    elif (s[i+1] == 'C'):
                        num += 90
                        i += 1
                    else:
                        num += 10
                else:
                    num += 10
            elif (s[i] == 'C'):
                if (i != (len(s)-1)):
                    if (s[i+1] == 'D'):
                        num += 400
                        i += 1
                    elif (s[i+1] == 'M'):
                        num += 900
                        i += 1
                    else:
                        num += 100
                else:
                    num += 100
            else:
                num += self.dict[s[i]]
            i += 1
        return num
        
        
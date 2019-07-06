class Solution:
    def romanToInt(self, s: str) -> int:
        
        number = 0
        i = 0
        
        while i < (len(s)):
            if s[i] == 'M':
                number += 1000
                i += 1
            elif s[i] == 'D':
                if i+1 < len(s) and s[i+1] == 'M':
                    number +=500
                    i+=2
                else:
                    number += 500
                    i+=1
            elif s[i] == 'C':
                if i+1 < len(s) and s[i+1] == 'M':
                    number +=900
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'D':
                    number +=400
                    i+=2
                else:
                    number +=100
                    i+=1
            elif s[i] == 'L':
                if i+1 < len(s) and s[i+1] == 'M':
                    number +=950
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'D':
                    number +=450
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'C':
                    number +=50
                    i+=2
                else:
                    number +=50
                    i+=1
            elif s[i] == 'X':
                if i+1 < len(s) and s[i+1] == 'M':
                    number +=990
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'D':
                    number +=490
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'C':
                    number +=90
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'L':
                    number +=40
                    i+=2
                else:
                    number +=10
                    i+=1
            elif s[i] == 'V':
                if i+1 < len(s) and s[i+1] == 'M':
                    number +=995
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'D':
                    number +=495
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'C':
                    number +=95
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'L':
                    number +=45
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'X':
                    number +=5
                    i+=2
                else:
                    number +=5
                    i+=1
            elif s[i] == 'I':
                if i+1 < len(s) and s[i+1] == 'M':
                    number +=999
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'D':
                    number +=499
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'C':
                    number +=99
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'L':
                    number +=49
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'X':
                    number +=9
                    i+=2
                elif i+1 < len(s) and s[i+1] == 'V':
                    number +=4
                    i+=2
                else:
                    number +=1
                    i+=1
            
        return number
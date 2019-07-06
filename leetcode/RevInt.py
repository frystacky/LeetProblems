class Solution:
    def reverse(self, x: int) -> int:
          
        isNeg = False
        
        if x < 0:
            isNeg = True
            x = x * -1
        
        oldNum = x
        newNum = 0
        modNum = 0
        
        while oldNum != 0:
            modNum = oldNum % 10
            oldNum = int(oldNum/10)
            newNum = (newNum * 10) + modNum
            
        if isNeg:
            newNum = newNum * -1
            
        if (newNum > (2**31)-1) or (newNum < (-2**31)):
            return 0   
        
        return newNum
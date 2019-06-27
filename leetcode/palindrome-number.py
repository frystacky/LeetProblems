class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        target = str(x)
        
        if target == target[::-1]:
            return True
        else:
            return False
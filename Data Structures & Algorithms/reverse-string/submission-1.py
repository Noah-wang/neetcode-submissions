class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s) // 2
        left = 0
        right = len(s)-1
        for i in range(len(s)):
                tep = s[left]
                s[left] = s[right]
                s[right] =tep 
                left +=1
                right -=1
                if right < left:
                    break
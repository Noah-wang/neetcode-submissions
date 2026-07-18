class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans += [num]
        for num in nums:
            ans += [num]   
        return ans
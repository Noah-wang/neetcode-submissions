class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sortedArray = sorted(nums)
        middle = len(sortedArray) // 2
        return sortedArray[middle] 
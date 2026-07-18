class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = 0
        fast = len(numbers) -1
        while slow < fast:
            curSum = numbers[slow] + numbers[fast]
            if curSum < target:
                slow += 1
            elif curSum > target:
                fast -= 1
            else:
                return [slow + 1, fast + 1]
        return []
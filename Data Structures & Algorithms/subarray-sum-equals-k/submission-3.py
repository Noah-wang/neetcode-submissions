class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prev_sum = 0
        prev_count = {0:1}
        for num in nums:
            prev_sum += num
            need = prev_sum - k
            
            if need in prev_count:
                count += prev_count[need]


            prev_count[prev_sum] = prev_count.get(prev_sum, 0) + 1
        return count
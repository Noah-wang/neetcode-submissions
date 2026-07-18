class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        while l < r:
            mid = (l + r) //2
            groups = 1
            cur = 0

            for num in nums:
                if cur + num <= mid:
                    cur +=num
                else:
                    groups +=1
                    cur = num
            if groups <= k:
                r = mid
            else:
                l = mid +1

        return l
                
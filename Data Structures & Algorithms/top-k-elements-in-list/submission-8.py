class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        items = list(count.items())
        items.sort(key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(items[i][0])

        return res
        
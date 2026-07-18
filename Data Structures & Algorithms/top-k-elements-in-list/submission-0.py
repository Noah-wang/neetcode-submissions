class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] +=1
        items = list(dict.items())
        items.sort(key = lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(items[i][0])
        return res
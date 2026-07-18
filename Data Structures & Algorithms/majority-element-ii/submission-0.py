class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        length = len(nums)
        dict = {}
        list = []
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] +=1

            if dict[num] > length/3 and num not in list:

                list.append(num)
        return list
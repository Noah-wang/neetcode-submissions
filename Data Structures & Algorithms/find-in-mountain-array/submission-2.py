class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) //2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid +1
            else:
                r = mid -1
        
        peak = l
        l = 0
        r = peak
    
        while l <= r:
            mid = (l + r) //2
            value = mountainArr.get(mid)
            if value == target:
                return mid
            elif value < target:
                l = mid + 1
            else:
                r = mid -1


        l = peak + 1
        r = n -1
    
        while l <= r:
            mid = (l + r) //2
            value = mountainArr.get(mid)
            if value == target:
                return mid
            elif value < target:
                r = mid -1
            else:
                l = mid + 1

        return -1

        
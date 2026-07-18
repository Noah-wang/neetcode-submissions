class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = (l + r) //2
            
            used_day = 1
            current_weight = 0

            for w in weights:
                if current_weight + w > mid:
                    used_day += 1
                    current_weight =0
                
                current_weight += w
            
            if used_day <= days:
                r = mid
            else:
                l = mid +1
        return l

        
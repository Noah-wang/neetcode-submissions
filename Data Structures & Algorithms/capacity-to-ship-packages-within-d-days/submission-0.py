class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = (l + r) //2

            used_days = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight > mid:
                    used_days +=1
                    current_weight = 0
                
                current_weight += weight
            
            if used_days <= days:
                r = mid
            else:
                l = mid +1

        return l
            

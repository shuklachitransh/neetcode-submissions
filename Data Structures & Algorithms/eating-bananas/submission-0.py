import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(speed,piles):
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / speed)
            return total_time
        
        i , j = 1 , max(piles)
        while i < j :
            mid = i + (j-i) // 2
            total_time = valid(mid,piles)

            if total_time <= h:
                j = mid
            else:
                i = mid + 1
        return i

            




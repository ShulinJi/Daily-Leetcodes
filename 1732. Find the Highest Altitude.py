class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_point = 0
        total_altitude = 0
        for x in gain:
            total_altitude += x
            max_point = max(max_point, total_altitude)
        
        return max_point

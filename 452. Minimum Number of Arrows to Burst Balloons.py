class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # we merge the intervals and take their overlap part for the new merged interval
        points.sort(key=lambda x: x[0])

        overlap = []
        for interval in points:
            if not overlap or overlap[-1][1] < interval[0]:
                overlap.append(interval)
            else:
                overlap[-1] = [max(interval[0], overlap[-1][0]), min(interval[1], overlap[-1][1])]
            
        return len(overlap)




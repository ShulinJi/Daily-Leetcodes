class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        res1 = []
        res2 = []

        for x in set1:
            if x not in set2:
                res1.append(x)
        for x in set2:
            if x not in set1:
                res2.append(x)
        return [res1, res2]

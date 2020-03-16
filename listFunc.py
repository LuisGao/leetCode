class Solution:
    def __init__(self):
        a = 1
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        set1 = set()
        set2 = set()
        dict1 = {}
        dict2 = {}
        for a in A:
            for b in B:
                set1.add(a+b)

        for c in C:
            for d in D:
                set2.add(-c-d)

        set3 = set1 & set2
        return len(set3)


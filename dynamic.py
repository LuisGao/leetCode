from math import *
class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rnum = 0
        nums.sort()
        p1 = 0
        p2 = 1
        p3 = 2
        le = len(nums)
        for p1 in range(le - 2):
            for p2 in range(p1 + 1, le - 1):
                bvld = False
                ma = nums[p1] + nums[p2]
                mi = abs(nums[p1] - nums[p2])
                pl = p2 + 1
                pr = le - 1
                while pr >= pl:
                    if nums[pl] > mi and nums[pr] < ma:
                        bvld = True
                        break
                    if nums[pl] <= mi:
                        pl += 1
                    if nums[pr] >= ma:
                        pr -= 1
                if bvld:
                    rnum += pr - pl + 1
        return rnum
    def getPermutation(self, n, k):
        ren = []
        jcl = []
        rl = ''
        k -= 1
        for i in range(n):
            ren.append(i + 1)
            jcl.insert(0, factorial(i))
        p = 0
        while len(ren) > 0:
            td = int(k / jcl[p])
            tn = int(k % jcl[p])
            rl += str(ren[td])
            del ren[td]
            k = tn
            p += 1
        return rl
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reCount = 0
        tm = 0
        for n in nums:
            if n == 1:
                tm += 1
            else:
                reCount = max(reCount, tm)
                tm = 0
        reCount = max(reCount, tm)
        return reCount

s = Solution()
#print(s.triangleNumber([1, 2, 3, 4]))
#print(s.getPermutation(9,15432))
print(s.findMaxConsecutiveOnes([1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1]))
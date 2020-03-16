
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reList = [0, 0]
        le = len(s)
        tlen = 0
        if le < 3:
            return s
        # 判断基数
        r = 1
        for c in range(1, le - 1):
            while c >= r and c + r < le and s[c - r] == s[c + r]:
                r += 1
            r -= 1
            if tlen < r * 2 + 1:
                tlen = r * 2 + 1
                reList = [c - r, c + r]
            r = 1

        # 判断偶数
        for c in range(0, le - 1):
            if s[c] == s[c + 1]:
                while c >= r and c + r + 1 < le and s[c - r] == s[c + 1 + r]:
                    r += 1
                r -= 1
                if tlen < r * 2 + 2:
                    tlen = r * 2 + 2
                    reList = [c - r, c + 1 + r]
                r = 1
        return s[reList[0]:reList[1] + 1]

    def isThreeUp(self, nums):
        pair = []
        tp = [ ]
        le = len(nums)

        for i in range(1, le + 1):
            if i < le and nums[i] > nums[i - 1]:
                if len(tp) < 2:
                    if len(tp) == 0:
                        tp = [nums[i - 1], nums[i]]
                else:
                    return True
            else:
                if len(tp) == 2:
                    if len(pair) == 0:
                        pair.append(tp[0])
                        pair.append(tp[1])
                    else:
                        if tp[1] > pair[1]:
                            return  True
                        elif tp[0] > pair[0]:
                            return True
                        elif tp[1] > pair[0]:
                            pair[1] = tp[1]
                        elif tp[0] < pair[0]:
                            pair[0] = tp[0]
                    tp.clear()
        return False

    def findMedianSortedArrays(self, nums1, nums2):



s = Solution()
#print(s.longestPalindrome("adfecvja;lkrjgdcedwesx"))
b = s.isThreeUp([1,0,0,0,0,0,0,00,0,0,0,0,0,00,10,0,0,0,0,0,100])
print(b)

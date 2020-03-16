class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        reList = [[1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        ll = [0, 1, 0]
        for i in range(2, numRows + 1):
            temp = [0] * (i + 2)
            for j in range(1, i + 1):
                temp[j] = ll[j - 1] + ll[j]
            ll = temp
            reList.append(temp[1:i+1])
        print(reList)

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        cols = []
        rows = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols.append(j)
                    rows.append(i)
        for col in cols:
            for item in matrix:
                item[col] = 0
        for row in rows:
            matrix[row] = [0]*n
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p1 = 0
        p2 = 1
        maxlen = 1
        lenth = len(s)
        if lenth < 2:
            return 1
        while p2 < lenth:
            if s[p2] in s[p1:p2]:
                p0 = s[p1:p2].index(s[p2])
                p1 = p1 + p0 + 1
            else:
                if p2 - p1 + 1> maxlen:
                    maxlen = p2 - p1 + 1
            p2 += 1
        return maxlen
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.str = s
        self.pl = 0
        self.pr = 0
        p1 = 0
        p2 = len(s) - 1
        self.judgeSame(p1, p2)
        print(self.pl)
        print(self.pr)
        r = min(len(s) - 1, self.pr + 1)

        return s[self.pl:self.pr + 1]


    def judgeSame(self, p1, p2):
        if p1 == p2:
            return True
        else:
            if self.str[p1] == self.str[p2]:
                if p2 - p1 >= self.pr - self.pl and self.judgeSame(p1 + 1, p2 - 1):
                    self.pl = p1
                    self.pr = p2
                    return True
            else:
                self.judgeSame(p1 + 1, p2)
                self.judgeSame(p1, p2 - 1)
                return False

s = Solution()
matrix = [[1,2,4,0], [2,3,4,5]]
#s.setZeroes(matrix)
a = s.longestPalindrome("babadada")
b= 1
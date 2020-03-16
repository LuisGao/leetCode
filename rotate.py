class Solution:
    def spiralOrder(self):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        matrix = [[3],[2]]
        reList = []
        delType = 0
        while matrix != []:
            self.delMatrix( matrix, reList, delType)
            delType += 1
            delType = delType % 4

        print(reList)
        return reList

    def delMatrix(matrix, reList, delType):
        if len(matrix) == 0:
            return
        elif len(matrix[0]) == 0:
            del matrix[0]
            return
        if delType == 0:
            tl = matrix[0]
            for i in tl:
                reList.append(i)
            del matrix[0]
        elif delType == 1:
            for row in matrix:
                reList.append(row[len(row) - 1])
                del row[len(row) - 1]
        elif delType == 2:
            lenth = len(matrix)
            tl = matrix[lenth - 1]
            for i in range(len(matrix[0])):
                reList.append(tl[len(matrix[0]) - 1 - i])
            del matrix[lenth - 1]
        else:
            lenth = len(matrix)
            for i in range(lenth):
                reList.append(matrix[lenth - 1 - i][0])
                del matrix[lenth - 1 -i][0]


s = Solution
l1 = [1,2,4]

a = s.spiralOrder(s)
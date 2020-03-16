class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        isUp = False
        upList = []
        sum = 0
        for i in range(1, len(prices)):
            if not isUp and prices[i] > prices[i - 1]:
                nl = [prices[i - 1]]
                upList.append(nl)
                isUp = True
            elif isUp and prices[i] < prices[i - 1]:
                isUp = False
                nl = upList[len(upList) - 1]

        for pa in upList:
            sum += pa[1] - pa[0]

        return sum

s = Solution()
print(s.maxProfit([1,2]))

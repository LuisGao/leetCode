class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        tempIntStr = ''
        tempStr = ''
        tempIntStack = []
        tempStrStack = []

        reStr = ''
        bisn = False

        for c in s:
            if c.isnumeric() and bisn:
                tempIntStr += c
            elif c == '[':
                tempIntStack.insert(0, tempIntStr)
                tempIntStr = ''
                tempStrStack.insert(0, '')
                bisn = False
            elif c == ']':

                if len(tempStr) > 0:
                    tempStrStack[0] = tempStrStack[0] + tempStr
                    tempStr = ''
                ts = tempStrStack[0]
                del tempStrStack[0]
                ti = int(tempIntStack[0])
                del tempIntStack[0]
                tss = ''
                for i in range(ti):
                    tss += ts
                if len(tempStrStack) == 0:
                    reStr += tss
                else:
                    tempStrStack[0] = tempStrStack[0] + tss

            elif c.isnumeric() and not bisn:
                tempIntStr += c
                if len(tempIntStack) == 0:
                    reStr += tempStr
                else:
                    tempStrStack[0] = tempStrStack[0] + tempStr
                tempStr = ''
                bisn = True
            else:
                tempStr += c
        reStr += tempStr
        return reStr
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for s in S:
            if J.find(s) != -1:
                count += 1
        return count
    def getMax(self, n):
        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            


s = Solution()
print(s.decodeString('3[z]2[2[y]pqef]'))
print(s.numJewelsInStones('Aa', 'asDBADDDdd'))
#zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef
class Solution:
    def myAtoi(self, str: str) -> int:
        """
            考虑循环遍历判断
            假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，返回                       INT_MAX (231 − 1) 或 INT_MIN (−231) 。
        """
        str = str.strip()

        if not str:
            return 0

        isPos = None

        if str[0] == '+' or str[0] == '-':
            if str[0] == '+':
                isPos = True
            if str[0] == '-':
                isPos = False
            str = str[1:]

        strNum = 0

        for char in str:
            if char >= '0' and char <= '9':
                strNum = strNum * 10 + ord(char) - ord('0')
            else:
                break

        if strNum > 2147483647:
            if isPos == False:
                return -2147483648
            else:
                return 2147483647
        if isPos == False:
            strNum = -1 * strNum

        return strNum

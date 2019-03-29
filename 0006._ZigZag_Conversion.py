<<<<<<< HEAD
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
            假设当前行数是r，总行数R，I(n)表示某行第n个字母在原字符串中的index，n从0开始：
            r=1,R时，I(n+1) = I(n)+2(R-1)
            1<r<R时，
            I(n+1) = I(n)+2(R-r) n为偶数时，
            I(n+1) = I(n)+2(r-1) n为奇数
        """

        # 按行排序
        z = 0
        f = True
        if numRows == 1:
            return s
        tmp = ["" for i in range(numRows)]
        for i in s:
            tmp[z] += i
            if z == (numRows - 1) or z == 0: f = not f
            z = z - 1 if f else z + 1
=======
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
            假设当前行数是r，总行数R，I(n)表示某行第n个字母在原字符串中的index，n从0开始：
            r=1,R时，I(n+1) = I(n)+2(R-1)
            1<r<R时，
            I(n+1) = I(n)+2(R-r) n为偶数时，
            I(n+1) = I(n)+2(r-1) n为奇数
        """

        # 按行排序
        z = 0
        f = True
        if numRows == 1:
            return s
        tmp = ["" for i in range(numRows)]
        for i in s:
            tmp[z] += i
            if z == (numRows - 1) or z == 0: f = not f
            z = z - 1 if f else z + 1
>>>>>>> bebc8612da16ca8e407398a44eba42627767ace0
        return "".join(tmp)
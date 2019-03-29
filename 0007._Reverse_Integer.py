class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or -10 < x < 10:
            return (x)
        #         else:
        #             y = list(str(x))
        #             z = None
        #             for i in range(0,len(y)/2):
        #                 z = y[i]
        #                 y[i] = y[len(y)-1-i]
        #                 y[len(y)-1-i] = z
        #             z = ''
        #             for i in range(0,len(y)):
        #                 z += y[i]
        #             if X > 0:
        #                 z = int(z)
        #                 if z > 2147483646：
        #                     return(0)
        #             if x < 0:
        #                 z = int(z)
        #                 if z > 2147483647：
        #                     return(0)
        #                 z = '-' + z
        #             z = int(z)

        #             return(z)
        str_x = str(x)
        if str_x[0] != "-":
            # 不是负号则直接反转
            str_x = str_x[::-1]
            # str转为int
            x = int(str_x)
        else:
            # 是负号，则反转负号之后的字符串
            str_x = str_x[1:][::-1]
            # str转int
            x = int(str_x)
            # 加上负号
            x = -x
        # 三目运算符，判断是否溢出
        # 如果-2147483648 < x < 2147483647则返回x，否则返回0
        return x if -2147483648 < x < 2147483647 else 0


"""
    将字符串以数组处理
    因为  len(n) + len(m) <= len(n*m)
    所以可以新建一个数组num3,长度m+n(python不需要)

    1:先计算保存，再进位
    2:计算时进位

    num1的第i位(高位从0开始)和num2的第j位相乘的结果在乘积中的位置是[i+j, i+j+1]
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ""
        dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        num3 = []
        for i in range(len(num1) + len(num2)):
            num3.append(0)

        # 倒序遍历太麻烦了，直接num1 num2 逆序
        # num1 = num1[::-1]
        # num2 = num2[::-1]
        for i in range(len(num1) - 1, -1, -1):
            target = 0
            for j in range(len(num2) - 1, -1, -1):
                bitmul = dic[num1[i]] * dic[num2[j]]
                bitmul += num3[i + j + 1]  # 先加低位判断是否有进位

                num3[i + j] += bitmul // 10
                num3[i + j + 1] = bitmul % 10
        num3 = "".join(str(i) for i in num3).lstrip('0')

        return '0' if num3 == '' else num3
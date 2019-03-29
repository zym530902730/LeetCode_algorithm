<<<<<<< HEAD
class Solution:
    def romanToInt(self, s: str) -> int:
        #         data1 = {
        #             'IV':4,
        #             'IX':9,
        #             'XL':40,
        #             'XC':90,
        #             'CD':400,
        #             'CM':900
        #         }
        #         data2 = {
        #             'I':1,
        #             'V':5,
        #             'X':10,
        #             'L':50,
        #             'C':100,
        #             'D':500,
        #             'M':1000
        #         }

        #         sum = 0

        # 通常小数字在大数字右边，但是有六种特殊情况
        #         for i in range(len(s)):
        #             if
        #             if i<len(s)-1 and s[i] < s[i+1]:
        #                 if s[i]+s[i+1] in data1:
        #                     sum += data1[s[i]+s[i+1]]
        #                 else:
        #                     sum += data2[s[i]]
        #             else:
        #                 sum += data2[s[i]]

        #         return sum

        #         if len(s) == 1:
        #             return data2[s]
        #         else:
        #             for i in range(0,len(s)-1):
        #                 if s[i]+s[i+1] in data1:
        #                     sum += data1[s[i]+s[i+1]]
        #                     if i==len(s)-1:
        #                         return sum

        #                 if i<len(s)-1 and s[i] > s[i+1]:
        #                     if i>=1 and s[i-1]+s[i] in data1:
        #                         continue
        #                     else:
        #                         sum += data2[s[i]]
        #                         if i==len(s)-1:
        #                             sum += data2[s[i+1]]
        #                         return sum
        #             return sum
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
=======
class Solution:
    def romanToInt(self, s: str) -> int:
        #         data1 = {
        #             'IV':4,
        #             'IX':9,
        #             'XL':40,
        #             'XC':90,
        #             'CD':400,
        #             'CM':900
        #         }
        #         data2 = {
        #             'I':1,
        #             'V':5,
        #             'X':10,
        #             'L':50,
        #             'C':100,
        #             'D':500,
        #             'M':1000
        #         }

        #         sum = 0

        # 通常小数字在大数字右边，但是有六种特殊情况
        #         for i in range(len(s)):
        #             if
        #             if i<len(s)-1 and s[i] < s[i+1]:
        #                 if s[i]+s[i+1] in data1:
        #                     sum += data1[s[i]+s[i+1]]
        #                 else:
        #                     sum += data2[s[i]]
        #             else:
        #                 sum += data2[s[i]]

        #         return sum

        #         if len(s) == 1:
        #             return data2[s]
        #         else:
        #             for i in range(0,len(s)-1):
        #                 if s[i]+s[i+1] in data1:
        #                     sum += data1[s[i]+s[i+1]]
        #                     if i==len(s)-1:
        #                         return sum

        #                 if i<len(s)-1 and s[i] > s[i+1]:
        #                     if i>=1 and s[i-1]+s[i] in data1:
        #                         continue
        #                     else:
        #                         sum += data2[s[i]]
        #                         if i==len(s)-1:
        #                             sum += data2[s[i+1]]
        #                         return sum
        #             return sum
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
>>>>>>> bebc8612da16ca8e407398a44eba42627767ace0
        return ans
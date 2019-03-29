class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            中心扩展算法  我们观察到回文中心的两侧互为镜像。
            因此，回文可以从它的中心展开，并且只有 2n - 12n−1 个这样的中心。
            为什么会是 2n - 12n−1 个，而不是 nn 个中心？
            原因在于所含字母数为偶数的回文的中心可以处于两字母之间（例如 {“abba”} “abba” 的中心在两个‘b’‘b’ 之间）。



        """
        #         start,end = 0,0
        #         le = len(s)
        #         left,right = 0,0
        #         if le == 0:
        #             return s
        #         for i in range(0,le):
        #             left, right = i,i
        #             while left >=0 and right < le:
        #                 if s[left] == s[right]:
        #                     left -= 1
        #                     right += 1
        #                 else:
        #                     break
        #             len1 = right -left -1

        #             left, right = i, i+1
        #             while left >=0 and right < le:
        #                 if s[left] == s[right]:
        #                     left -= 1
        #                     right += 1
        #                 else:
        #                     break
        #             len2 = right -left -1

        #             l = len1 if len1 > len2 else len2
        #             if l > end-start:
        #                 start = i - (l-1)/2
        #                 end = i + (l)/2

        #         return s[int(start):int(end)+1]
        #         n = len(s)
        #         if n < 2:
        #             return s

        #         # left index of the target substring
        #         l = 0
        #         # right index of the target substring
        #         r = 0
        #         # length of the longest palindromic substring for now
        #         m = 0
        #         # length of the current substring
        #         c = 0

        #         # Whether the substring contains the first character or last character and is palindromic
        #         b = True
        #         for i in range(n):
        #             # Odd situation
        #             for j in range(min(n-i,i+1)):
        #                 if s[i-j] != s [i+j]:
        #                     b = False
        #                     break
        #                 else:
        #                     c = 2 * j + 1

        #             if c > m :
        #                 l = i - j + 1 - b
        #                 r = i + j + b
        #                 m = c
        #             b = True

        #             # Even situation
        #             for j in range(min(n - i - 1, i + 1)):
        #                 if (s[i - j] != s[i + j + 1]):
        #                     b = False
        #                     break
        #                 else:
        #                     c = 2 * j + 2
        #             if (c > m):
        #                 l = i - j + 1 - b
        #                 r = i + j + 1 + b
        #                 m = c
        #             b = True
        #         return s[l:r]
        start, maxl = 0, 0
        for i in range(len(s)):
            if i - maxl >= 1 and s[i - maxl - 1:i + 1] == s[i - maxl - 1:i + 1][::-1]:
                start = i - maxl - 1
                maxl += 2
            if i - maxl >= 0 and s[i - maxl:i + 1] == s[i - maxl:i + 1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start:start + maxl]
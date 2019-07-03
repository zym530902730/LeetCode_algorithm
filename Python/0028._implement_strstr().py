# 暴力破解法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle) and haystack[i + j] == needle[j]:
                    j += 1
                if j == len(needle):
                    return i
        return -1


# KMP算法
# 来自网络
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        text, pattern = haystack, needle
        if not pattern or len(pattern) == 0:
            return 0

        lps = self.findLPS(pattern)  # longest proper prefix which is also suffix
        i, j = 0, 0  # idx for text and pattern
        res = -1
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                res = i - j
                return res
                j = lps[j - 1]
            elif i < len(text) and pattern[j] != text[i]:  # mismatch after j matches
                if j != 0:  # Don't match lps[0..lps[j-1]] characters, they will match anyway
                    j = lps[j - 1]
                else:
                    i += 1
        return res

    def findLPS(self, pattern):
        length, lps = 0, [0]
        for i in range(1, len(pattern)):
            while length > 0 and pattern[length] != pattern[i]:
                length = lps[length - 1]
            if pattern[length] == pattern[i]:
                length += 1
            lps.append(length)
        return lps
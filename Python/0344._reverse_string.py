class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = list(s)
        start, end = 0, len(lst) - 1

        while start < end:
            lst[end], lst[start] = lst[start], lst[end]
            start += 1
            end -= 1
        return ''.join(lst)
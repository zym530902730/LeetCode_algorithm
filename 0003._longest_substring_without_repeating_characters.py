<<<<<<< HEAD
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        li = []
        i = 0
        j = 0
        while i < len(s):
            if s[i] not in li:
                li.append(s[i])
                #print(li)
                i += 1
            else:
                count = max(len(li) ,count)
                j = li.index(s[i])
                li = li[j+1:]
        count = max(len(li), count)
=======
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        li = []
        i = 0
        j = 0
        while i < len(s):
            if s[i] not in li:
                li.append(s[i])
                #print(li)
                i += 1
            else:
                count = max(len(li) ,count)
                j = li.index(s[i])
                li = li[j+1:]
        count = max(len(li), count)
>>>>>>> bebc8612da16ca8e407398a44eba42627767ace0
        return count
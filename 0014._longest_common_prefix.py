class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num2 = ''

        if len(strs) == 1:
            return strs[0]
        if len(strs) == 0 or strs == ['']:
            return ""

        for index in range(len(strs[1]) if len(strs[0]) > len(strs[1]) else len(strs[1])):
            if strs[0][:index + 1] == strs[1][:index + 1]:
                num2 = strs[0][:index + 1]
            else:
                break
        if num2 == '':
            return num2

        for j in range(1, len(strs)):
            num3 = ''
            for index in range(len(num2)):

                if strs[j][:index + 1] == num2[:index + 1]:
                    num3 = num2[:index + 1]
                else:
                    num2 = num3
                    break

        return num2
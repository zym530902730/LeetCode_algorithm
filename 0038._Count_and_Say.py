class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for i in range(2, n + 1):
            result_now = ''
            now = ''
            for char in result:
                if now == '':
                    now = char
                    continue
                if char == now[0]:
                    now = now + char
                else:
                    result_now += str(len(now)) + now[0]
                    now = char
            result_now += str(len(now)) + now[0]
            result = result_now
        return result
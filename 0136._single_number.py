class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
            交换律：a ^ b ^ c <=> a ^ c ^ b

            任何数于0异或为任何数 0 ^ n => n

            相同的数异或为0: n ^ n => 0
        """
        # a = 0
        # for n in nums:
        #     a = a ^ n
        # return a

        # 脑筋急转弯型：
        set1 = list(set(nums))
        sum1 = sum(set1)
        sum2 = sum(nums)
        return 2 * sum1 - sum2
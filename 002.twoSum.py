"""

"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        l = head
        carry = 0
        # 当两个链表为空并且无进位，则退出循环
        while l1 or l2 or carry:
            # 每次循环开始，将进位给sum，并且进位清零
            sum, carry = carry, 0
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            # 如果sum大于9，则进位
            if sum > 9:
                carry = 1
                sum -= 10
            # 创建新节点
            l.next = ListNode(sum)
            l = l.next
        return head.next
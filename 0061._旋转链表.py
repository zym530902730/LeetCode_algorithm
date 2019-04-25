# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        # 尾部向前数第K个元素作为头，原先的头接到原先的尾上
        lenth = 0
        temp = head
        while temp:
            temp = temp.next
            lenth += 1

        step = lenth - k % lenth

        if step == 0 or step == lenth:
            return head

        # 根据step向后移动指针，新尾指向空，生成新头
        temp = head
        old_head = head
        while step > 0:
            if step == 1:
                new_tail = temp
                temp = temp.next
                new_tail.next = None
            else:
                temp = temp.next
            step -= 1
        new_head = temp

        # 向后移动指针，找到旧尾指向旧头
        while temp:
            if temp.next is None:
                temp.next = old_head
                break
            else:
                temp = temp.next

        return new_head

# 网络版
# 时间复杂度: O(N)- 空间复杂度: O(1)
# k可能比list的size大，需要做一个取余准备
# 计算list size的同时把tail也记录下来，方便之后把tail的next指向原本的head
# 利用之前的到末端的kth node
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        size = 0
        cur = tail = head
        while cur:
            size += 1
            tail = cur
            cur = cur.next

        k = k % size
        if k == 0:
            return head

        tmp = self.findLastKth(head, k, size)
        last_kth = tmp.next
        tmp.next = None
        tail.next = head
        return last_kth

    def findLastKth(self, node, k, size):
        for i in range(size - k - 1):
            node = node.next
        return node
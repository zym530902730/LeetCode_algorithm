# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
时间复杂度: O(N)- 空间复杂度: O(N)
InOrder排序，输出，当然也完全可以用昨天的binary tree iterator,入stack,出stack,直到输出第k位
"""


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.root = root
        self.lst = []
        self.inOrder(root)
        return self.lst[k-1]

    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        self.lst.append(root.val)
        self.inOrder(root.right)


# yield
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def gen(r):
            if r is not None:
                yield from gen(r.left)
                yield r.val
                yield from gen(r.right)

        it = gen(root)
        for _ in range(k):
            ans = next(it)
        return ans



"""

现在看到kth 就条件反射的想用divide & conquer, 扫root的左子树看nodes量，如果nodes数量是k-1，那么root就刚好是第k个，如果大于k > 左子树数量，扫右子树，同时更新root为root.right。
if k == node.leftNum + 1, return node
if k > node.leftNum + 1, make k -= node.leftNum + 1, and then node = node.right
otherwise, node = node.left

"""
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def count(node):
            if not node:
                return 0
            return count(node.left) + count(node.right) + 1

        if not root:
            return None
        left = count(root.left)
        if left == k - 1:
            return root.val
        elif left > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - left - 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 暴力遍历
# 时间复杂度: O(N)- 空间复杂度: O(N)
class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        if not root:
            return 0

        stack = []
        node = root
        while node or (len(stack) > 0):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return len(res)


# 分治法 递归
# 时间复杂度: O(N)- 空间复杂度: O(1)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)



# 时间复杂度: O(lgN * lgN) - 空间复杂度: O(1) ** ** **

"""
求出正常的左右子树的高度lh和rh，然后

如果相等的话就知道左边子树肯定是满的，一共有2 ** lh个node，先算出来然后递归计算右边子树的node个数；
同理lh和rh不相等的话，就知道右边子树是满的，一共有2 ** rh个node，先算出来然后递归计算右边子树的node个数；
"""

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        if lh == rh:
            return 2 ** lh + self.countNodes(root.right)
        else:
            return 2 ** rh + self.countNodes(root.left)

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


# 时间复杂度: O(lgN * lgN)- 空间复杂度: O(1)******
"""
既然说了是 complete binary tree，那么必然有特性可用，complete binary tree的特性是除了最后一层，之前的就是perfect tree.

所以寻找左子树的最左边的高度left_most_height和右子树的最右边的node高度right_most_height，如果相同就是perfect tree，高度2^h - 1， 否则递归的来看左子树和右子树

"""

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        p, q = root, root

        lmh, rmh = 0, 0
        while p:
            p = p.left
            lmh += 1
        while q:
            q = q.right
            rmh += 1

        if lmh == rmh:
            return 2 ** lmh - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
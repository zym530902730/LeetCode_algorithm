<<<<<<< HEAD
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            l = self.maxDepth(root.left) + 1
            r = self.maxDepth(root.right) + 1
=======
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            l = self.maxDepth(root.left) + 1
            r = self.maxDepth(root.right) + 1
>>>>>>> bebc8612da16ca8e407398a44eba42627767ace0
            return max(l,r)
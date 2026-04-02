# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        GLOBAL_MIN = -float('inf')
        GLOBAL_MAX = float('inf')
        self.isBST = False

        def dfs(curr, minimum, maximum):
            if not curr:
                return True

            if not (minimum < curr.val < maximum):
                return False

            # valBalanced = (curr.left.val > minimum and curr.left.val < curr.val and curr.right.val > curr.val and curr.right.val < maximum)
            leftBST = dfs(curr.left, minimum, curr.val)
            rightBST = dfs(curr.right, curr.val, maximum)

            return (leftBST and rightBST)

        return dfs(root, GLOBAL_MIN, GLOBAL_MAX)

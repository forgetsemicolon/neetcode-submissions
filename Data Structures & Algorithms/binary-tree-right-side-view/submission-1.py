# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []

        # for each level
        while q:
            rightSide = None
            qLen = len(q)

            # until we have covered all the nodes in the particular level
            for i in range(qLen):
                # remove nodes from current level
                node = q.popleft()
                if node:
                    rightSide = node
                    # append nodes for next level (order matters)
                    q.append(node.left)
                    q.append(node.right)

            # append the rightmost node to the result 
            if rightSide:
                res.append(rightSide.val)

        return res
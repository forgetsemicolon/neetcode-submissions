# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
            
        if root.val == key:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = root.right
                while successor.left:
                    successor = successor.left
                
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            root.right = self.deleteNode(root.right, key)

        return root 


        # if not root:
        #     return None

        # dummy = TreeNode()

        # if root.val == key:
        #     dummy = root
        #     if root.left:
        #         root = root.left
        #         root.right = dummy.right
        #     elif root.right:
        #         root = root.right
        #         root.left = dummy.left
        #     else:
        #         root = None

        # elif key < root.val:
        #     root.left = self.deleteNode(root.left, key)

        # else:
        #     root.right = self.deleteNode(root.right, key)

        # return root 
        
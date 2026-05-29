# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []

    #     self.inorder(root, res)

    #     return res
    
    # def inorder(self, root: Optional[TreeNode], res: List[int]):
    #     if not root:
    #         return
        
    #     self.inorder(root.left, res)
    #     res.append(root.val)
    #     self.inorder(root.right, res)
        
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
            
        return res



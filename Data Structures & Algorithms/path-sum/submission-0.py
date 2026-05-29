# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        cur = targetSum - root.val

        if not root.left and not root.right:
            if cur == 0:
                return True
            else:
                return False
            
        if self.hasPathSum(root.left, cur):
            return True
        if self.hasPathSum(root.right, cur):
            return True
        return False


        

        
        
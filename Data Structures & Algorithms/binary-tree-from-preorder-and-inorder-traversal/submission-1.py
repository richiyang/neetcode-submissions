# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # p = i = 0
        
        # def dfs(limit):
        #     nonlocal p, i
        #     if p >= len(preorder):
        #         return None
        #     if inorder[i] == limit:
        #         i += 1
        #         return None
            
        #     root = TreeNode(preorder[p])
        #     p += 1
        #     root.left = dfs(root.val)
        #     root.right = dfs(limit)
        #     return root
        # return dfs(float('inf'))

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root


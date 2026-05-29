# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()

        if root:
            q.append(root)
        
        while q:
            right = -1
            for i in range(len(q)):
                cur = q.popleft()
                right = cur.val
                if cur.left:
                    q.append(cur.left)
                    right = cur.val
                if cur.right:
                    q.append(cur.right)
                    right = cur.val
            res.append(right)
        
        return res
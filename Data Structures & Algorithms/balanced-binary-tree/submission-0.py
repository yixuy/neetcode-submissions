# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.res = True 

        def traverse(curr):
            if not curr:
                return 0

            left_return = traverse(curr.left)
            right_return = traverse(curr.right)

            if abs(left_return - right_return) > 1:
                self.res = False

            return max(left_return, right_return) + 1

        traverse(root)
        return self.res
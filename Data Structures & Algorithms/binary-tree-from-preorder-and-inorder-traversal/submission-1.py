# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None 

        def traverse( preorder, inorder):
            if not preorder:
                return None 
            root = TreeNode(preorder[0])
            index = 0
            for i, num in enumerate(inorder):
                if num == preorder[0]:
                    index = i
            
            root.left = traverse(preorder[1: 1+index],inorder[:index])
            root.right = traverse(preorder[1+index:],inorder[index+1:])

            return root
    
        return traverse( preorder, inorder)


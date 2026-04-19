# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.

    # BFS



        # # if not root.left and not root.right:
        # #     return root.val
        # # res = root.val 

        # # if root.left:
        # #     res += BFS(root.left)
        # # if root.right:
        # #     res += BFS(root.right)

        # return res 

    def serialize(self, root: Optional[TreeNode]) -> str:
    
        if not root:
            return 'N'
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            curr = queue.popleft()
            if curr:
                res.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                res.append("N")

        return ",".join(res)
 
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        str_arr = data.split(',')
        if str_arr[0] == 'N':
            return None
            
        root = TreeNode()
        root.val = int(str_arr[0])
        curr = root
        queue = deque([root])
        index = 1
        
        while(queue):
            curr = queue.popleft()
            if str_arr[index] != 'N':
                curr.left =  TreeNode(int(str_arr[index]))
                queue.append(curr.left)
            index += 1

            if str_arr[index] != 'N':
                curr.right =  TreeNode(int(str_arr[index]))
                queue.append(curr.right)
            index += 1

        return root


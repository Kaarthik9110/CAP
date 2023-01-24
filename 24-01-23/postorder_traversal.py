class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def postorder(node):
            if not node:
                return 0
            else:
                postorder(node.left)
                postorder(node.right)
                res.append(node.val)
        postorder(root)
        return res

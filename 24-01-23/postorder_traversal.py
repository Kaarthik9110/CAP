class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def inorder(root):
            if not root:
                return
            else:
                inorder(root.left)
                inorder(root.right)
                res.append(root.val)
        inorder(root)
        return res

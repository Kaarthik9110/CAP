class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def preorder(root):
            if not root:
                return
            else:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return res

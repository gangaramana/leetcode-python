from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lis=[]
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            lis.append(root.val)
            inorder(root.right)
        inorder(root)
        r=None

        if(len(lis)>0):
            for i in lis:
                if r is None:
                    r=TreeNode(i)
                    continue
                x=r
                while(x.right is not None):
                    x=x.right
                x.right=TreeNode(i)

        return r




        # print(lis)


if __name__=="__main__":
    obj=Solution()
    root=TreeNode(5)
    root.left=TreeNode(3)
    root.left.left=TreeNode(2)
    root.left.right=TreeNode(4)
    root.left.left.left=TreeNode(1)
    root.right = TreeNode(6)
    root.right.right=TreeNode(8)
    root.right.right.left=TreeNode(7)
    root.right.right.right=TreeNode(9)
    p=obj.increasingBST(root)
    print(p.right+"  "+p.right.right)

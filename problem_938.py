import queue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def rangeSumBST(self, root, L, R):

        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        result = []
        su = [0]
        def inorder(root,L,R):
            if not root:
                return
            if(root.val>=L and root.val<=R):
                su[0] += root.val
            inorder(root.left, L, R)
            inorder(root.right, L, R)
        inorder(root, L, R)
        return su[0]





if __name__ == "__main__":


    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(6)
    root.right.righ = TreeNode(29)

    obj = Solution()
    L = 5
    R = 20
    x=obj.rangeSumBST(root, L, R)
    print(x)
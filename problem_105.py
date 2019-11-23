# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        count = len(postorder)-1
        if (len(postorder) > 0):
            node = TreeNode(postorder[count])
            ind = inorder.index(postorder[count])
            rig = inorder[ind + 1:]
            lef = inorder[:ind]

            def insert_right(root, right, y):
                no = None
                index = None
                for i in range(len(postorder[:y]),-1,-1):
                    z=postorder[i]
                    if (z in right):
                        no = z
                        index = right.index(no)
                        break
                while (root.right is not None):
                    root = root.right
                root.right = TreeNode(no)
                le = right[:index]
                ri = right[index + 1:]
                if (len(le) > 0):
                    insert_left(root.right, le, y - 1)
                if (len(ri) > 0):
                    insert_right(root.right, ri, y - 1)

            def insert_left(root, left, y):
                no = None
                index = None
                for i in range(len(postorder[:y-1]),-1,-1):
                    z=postorder[i]
                    if (z in left):
                        no = z
                        index = left.index(no)
                        break
                while (root.left is not None):
                    root = root.left
                root.left = TreeNode(no)
                le = left[:index]
                ri = left[index + 1:]
                if (len(le) > 0):
                    insert_left(root.left, le, y - 1)
                if (len(ri) > 0):
                    insert_right(root.left, ri, y - 1)

            if (len(lef) > 0):
                insert_left(node, lef, count)
            if (len(rig) > 0):
                insert_right(node, rig, count)

            return node


if __name__ == '__main__':
    obj=Solution()

    x=obj.buildTree([1,2,3,4],[4,3,2,1])
    print(x.right.right.val)

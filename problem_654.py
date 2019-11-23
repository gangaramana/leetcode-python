# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        index=nums.index(max(nums))
        right=nums[index+1:]
        left=nums[:index]
        root=TreeNode(nums[index])
        def right_insert(righ,treenode):
            ind = righ.index(max(righ))
            x=treenode
            while(treenode.right is not None):
                treenode=treenode.right
            treenode.right=TreeNode(righ[ind])
            le=righ[:ind]
            ri=righ[ind+1:]
            if(len(ri)>0):
                right_insert(ri,treenode.right)
            if(len(le)>0):
                left_insert(le,treenode.right)



            # if(len(no)>0):
            #     return
            # else:
            return treenode


        def left_insert(lef,treenode):
            ind = lef.index(max(lef))
            x = treenode
            while (treenode.left is not None):
                treenode = treenode.left
            treenode.left = TreeNode(lef[ind])
            le = lef[:ind]
            ri = lef[ind + 1:]
            if (len(ri) > 0):
                right_insert(ri, treenode.left)
            if (len(le) > 0):
                left_insert(le, treenode.left)
            return treenode
            # if (len(no) > 0):
            #     x=0
            #
            #
            # else:
            #     re=0

        if(len(right)>0):
            right_insert(right,root)

        if(len(left)>0):
            left_insert(left,root)


        return root







if __name__ == '__main__':
    obj=Solution()
    x=[3,2,1,6,0,5]
    y=obj.constructMaximumBinaryTree(x)
    print(y.right.val)
    # print(x.index(6))
    print(x[:3] ,"   ",x[6:])
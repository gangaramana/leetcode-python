from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        count=0
        if(len(preorder)>0):
            node=TreeNode(preorder[count])
            ind=inorder.index(preorder[count])
            rig=inorder[ind+1:]
            lef=inorder[:ind]
            def insert_right(root,right,y):
                no=None
                index=None
                for i in preorder[y+1:]:
                    if(i in right):
                        no=i
                        index=right.index(no)
                        break
                while(root.right is not None):
                    root=root.right
                root.right=TreeNode(no)
                le=right[:index]
                ri=right[index+1:]
                if(len(le)>0):
                    insert_left(root.right,le,y+1)
                if(len(ri)>0):
                    insert_right(root.right,ri,y+1)



            def insert_left(root,left,y):
                no=None
                inde=None
                for i in preorder[y+1:]:
                    if(i in left):
                        no=i
                        index=left.index(no)
                        break
                while(root.left is not None):
                    root=root.left
                root.left=TreeNode(no)
                le=left[:index]
                ri=left[index+1:]
                if(len(le)>0):
                    insert_left(root.left,le,y+1)
                if(len(ri)>0):
                    insert_right(root.left,ri,y+1)


            if(len(lef)>0):
                insert_left(node,lef,count)
            if(len(rig)>0):
                insert_right(node,rig,count)

            return node




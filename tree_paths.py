from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:



    def pre(self,t1,l2):
        if t1 is None:
            return
        else:
            l2.append(t1.val)
            self.pre(t1.left,l2)
            if(t1.left is None and t1.right is None):
                # if(sum(l2)==su):
                print(l2)
                l2.pop()
                return
            self.pre(t1.right,l2)

            l2.pop()



        # if not t1:
        #     return
        # if(t1.left == None and t1.right ==  None):
        #     li2+","+str(t1.val)
        #     print(li2)
        # self.pre(t1.left,li2+","+str(t1.val))
        # self.pre(t1.right,li2+","+str(t1.val))



    # def preorder(self,t,li):
    #     li.append(t.val)
    #     if(t.left is  None or t.right is None):
    #         print(li)
    #         if(t.left is not None):
    #             self.preorder(t.left,li)
    #     # li.pop()
    #     # li.append(t.val)
    #     if(t.right is not None):
    #         self.preorder(t.right, li)
    #     li.pop()

if __name__ == '__main__':
    obj=Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right=TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right=TreeNode(9000)
    l=[]
    # obj.preorder(root,l)
    # su=21
    obj.pre(root, l)





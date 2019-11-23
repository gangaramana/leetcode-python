# from collections import
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if(root is not None):
             list=[]
             min_dict={}
             dic={}
             list.append(root)
             while(list):
                 t=list.pop(0)
                 if(t==root):
                     dic[t]=1
                 if(t.left is not None):
                     dic[t.left]=dic[t]+1
                     list.append(t.left)
                 if(t.right is not None):
                     dic[t.right]=dic[t]+1
                     list.append(t.right)
                 if(t.right is None and t.left is None):
                     min_dict[t]=dic[t]
             l=min_dict.values()
             return min(l)
        return 0

if __name__=="__main__":
    obj=Solution()
    root=TreeNode(5)
    root.left=TreeNode(9)
    root.left.left=TreeNode(0)
    root.left.left.left=TreeNode(1)
    root.right=TreeNode(2)
    root.right.right=TreeNode(12)
    p=obj.minDepth(root)
    print(p)
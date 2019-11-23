from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root is not None):
            result=[[]]
            if(root is not None):
                 list=[]
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
                     # x=sorted(dic.items(), key=lambda x: x[1])
                 # print(x)
                 for k in range(max(dic.values())-1):
                     result.append([])

                 for i in dic.keys():
                     result[dic[i]-1].append(i.val)

            print(result)
            return result
        else:
            return []


if __name__=="__main__":
    obj=Solution()
    root = TreeNode(5)
    root.left = TreeNode(9)
    root.left.left = TreeNode(0)
    root.left.left.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(12)
    root.right.right.right = TreeNode(12)
    root.right.right.right.right = TreeNode(12)

    p = obj.levelOrder(root)
    # print(p)
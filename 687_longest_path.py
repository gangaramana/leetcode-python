# Definition for a binary tree node.
import queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if(root is not None):
            no=root.val
            di={}
            di[6]=0
            count=-1
            qu=queue.Queue()
            self.search(root,no,count,di,qu)
            return di


        else:
            return 0


    def search(self,treenode,search_no,cnt,dic,qu):
        if(treenode.val==search_no):
            cnt=cnt+1
        else:
            if(dic.get(search_no) is not None and dic.get(search_no) < cnt):
                dic.update({search_no:cnt})
            else:
                dic[search_no]=cnt
            cnt=0
            search_no=treenode.val
        if(treenode.left is not None):
            self.search(treenode.left, search_no, cnt, dic)
        if(treenode.right is not None):
            self.search(treenode.right,search_no,cnt,dic)




if __name__ == '__main__':
    obj=Solution()
    roo=TreeNode(5)
    roo.left=TreeNode(5)
    roo.right=TreeNode(1)
    roo.left.left=TreeNode(1)
    roo.left.left.left=TreeNode(1)
    roo.left.left.right=TreeNode(1)
    roo.left.right=TreeNode(12)
    roo.left.right.left=TreeNode(1)
    roo.left.right.right=TreeNode(1)
    roo.right.left=TreeNode(15)
    roo.right.right=TreeNode(1)
    roo.right.left.left=TreeNode(1)

    x=obj.longestUnivaluePath(roo)
    print(x)
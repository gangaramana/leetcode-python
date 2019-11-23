# import queue

class Solution:
    def titleToNumber(self, s: str) -> int:
        li=[]
        res=0
        # de=queue.Queue(len(s))
        for i in s:
            li.append(ord(i)-64)
            # de.append(ord(i)-64)
        k=len(s)-1
        while(k>=0):
            res=res+li[len(s)-1-k]*(26**k)
            # print("res   +li[k]*(26**k) ",res,"      ",li[k]*(26**k))
            k=k-1
        return res



if __name__ == '__main__':
    obj=Solution()
    re=obj.titleToNumber("AB")
    print(re)

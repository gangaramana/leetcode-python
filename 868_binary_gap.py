from  math import log


class Solution:
    def binaryGap(self, N: int) -> int:
        li=[]
        x=N
        while(x>0):
            no=int(log(x,2))
            li.append(no)
            x=x-2** no
            # if(x==0):
            #     return 0
            # else:
            #     return no-int(log(x,2))
        # print(li)
        max=0
        for i in range(len(li)-1):
            if(abs(li[i]-li[i+1]) >max):
                max=abs(li[i]-li[i+1])
        return max





if __name__ == '__main__':
    obj=Solution()
    x=obj.binaryGap(97)
    print(x)
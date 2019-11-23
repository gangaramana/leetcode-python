class Solution:
    def maximumSwap(self, num: int) -> int:
        l=str(num)
        print(type(l))
        i=0
        while(l[i]==max(l)):
            l.replace(max(l),'')
            i=i+1
        x=str(num).replace(max(l),min(l))

        if(len(str(num))>2):

        return int(x)


        # print(max(str(num)))
        # print(min(str(num)))











if __name__ == '__main__':
    obj=Solution()
    y=obj.maximumSwap(9090)
    print(y)
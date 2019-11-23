class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        # print(type(a[i]))
        k,sum=1,0
        while(i>=0 or j>=0):
            if(i>=0 and a[i]=="1"):
                sum=sum+k
            i=i-1
            if(j >= 0 and b[j]=="1"):
                sum=sum+k
            j=j-1
            k=k*2
        return bin(sum).replace("0b","")




if __name__ == '__main__':
    obj=Solution()
    b=obj.addBinary("111111","10101")
    print(b)
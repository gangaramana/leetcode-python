class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        while(sum!=1):
            sum=0
            for i in str(n):
                sum=sum+int(i)**2
            n=sum
        return True



if __name__ == '__main__':
    obj=Solution()
    x=obj.isHappy(70)
    print(x)
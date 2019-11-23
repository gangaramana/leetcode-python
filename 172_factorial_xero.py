class Solution:
    def trailingZeroes(self, n: int) -> int:
        x=n
        su=0
        while(x>0):
            su=su+int(x/5)
            x=int(x/5)
        # no = int(n / 5)
        return su



if __name__ == '__main__':
    obj=Solution()
    c=obj.trailingZeroes(56)
    print(c)


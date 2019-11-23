class Solution:
    def addDigits(self, num: int) -> int:
        if(num>10):
            n = num % 9
            if (n == 0):
                return 9
            else:
                return n
        return num



if __name__ == '__main__':
    obj=Solution()
    c=obj.addDigits(122321212)
    print(c)
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        flag=False
        sum=999
        li=[]
        for i in letters:
            v=ord(i)-ord(target)
            if(v<0):
                li.append(v)
            else:
                if(sum >v and v!=0):
                    sum=ord(i)-ord(target)
        if(sum==999):
            return chr(min(li)+ord(target))
        return chr(ord(target)+sum)





if __name__ == '__main__':
    obj=Solution()
    x=obj.nextGreatestLetter(['c','f','j'],'j')
    print(x)
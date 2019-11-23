from typing import  List

class Solution:
    def compress(self, chars: List[str]) -> int:
        count=1
        staring_no=0
        for i in range(len(chars)-1):
            if(chars[i]==chars[i+1]):
                count=count+1
            else:
                if(count>1):
                    for j in str(count):
                        staring_no=staring_no+1
                        chars[staring_no]=j
                    staring_no=staring_no+1
                    chars[staring_no]=chars[i+1]
                    count=1
                else:
                    staring_no=staring_no+1
                    chars[staring_no]=chars[i+1]


        if(count>1):
            for j in str(count):
                staring_no=staring_no+1
                chars[staring_no]=j
        return chars





if __name__=="__main__":
    obj=Solution()
    # a=["a","a","a","a","b","b","b","c","c","c"]
    a=["a","b","c","d","d","d","d","d","d","e","e","e"]
    print(a)
    x= obj.compress(a)
    # print(" the length is ",len(["a","a","a","a","b","b","b","c","c","c"]))
    print(x)
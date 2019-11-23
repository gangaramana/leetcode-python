# class Solution:
#     def nextGreaterElement(self, n: int) -> int:
#         string=str(n)
#         res=""
#         list=[]
#         for k in string:
#             list.append(k)
#         x=sorted(list)
#         print(x)
#         z=''
#         # res=None
#         for i in string:
#             index=x.index(i)
#             for z in x[index+1:]:
#                 if(z>i):
#                     break
#             if(z>i):
#                 res=res+z
#                 x.remove(z)
#                 break
#             else:
#                 res=res+i
#                 x.remove(i)
#         for n in x:
#             res=res+n
#         an=int(res)
#         # print(res)
#         # print(type(n))
#         if(int(n)<an and an <=2147483647):
#             return an
#         else:
#             return -1
#
#
#
#
#
#
#
#
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        li=[]
        # x=[]
        flag=False
        for i in str(n):
            li.append(i)
        print("prevvv  ",li)
        for j in range(len(li)-1,-1,-1):
            for k in range(j-1,-1,-1):
                if(li[k]<li[j]):
                    li=self.swap_list(li,k,li[j])
                    print("x    ",li)
                    flag=True
                    print(li)
                    break
            if(flag):
                break
        if(flag):
            # print((str(li)))
            k=""
            for i in li:
                k=k+i
            k=int(k)
            if(k>int(n) and k<2147483647):
                return k
        return -1





    def swap_list(self,list,no,value):
        for l in range(len(list)-1,no,-1):
            list[l]=list[l-1]
        list[no]=value
        print("in restlkndscsd",list)
        return list



if __name__ == '__main__':
    obj=Solution()
    p=obj.nextGreaterElement(8614)
    print(p)
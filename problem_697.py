class Solution(object):
   def findShortestSubArray(self, nums):
       general_dict={}
       duplicate_dict={}

       for i in nums:
           if(i in general_dict):
               general_dict[i]=general_dict[i]+1
               if(general_dict[i] in duplicate_dict):
                   duplicate_dict[general_dict[i]].append(i)
               else:
                   x=general_dict[i]
                   duplicate_dict[x]=[i]

           else:
               general_dict[i]=1
               if(1 in duplicate_dict):
                   duplicate_dict[1].append(i)
               else:
                   duplicate_dict[1]=[i]

       maxlen=max(duplicate_dict.keys())
       degree_list=duplicate_dict[maxlen]
       correct_list=nums.copy()
       nums.reverse()
       result_list=[]
       l=len(nums)
       for i in degree_list:
           x=l-nums.index(i)-correct_list.index(i)
           result_list.append(x)
       u=min(result_list)
       # print(u)
       return u
       # print(u)
       # print("nums     ",correct_list)
       # print("reverse   ",nums)
       # print("general_dict   ",general_dict )
       # print("duplicate_dict     ",duplicate_dict)






myobj=Solution()
myobj.findShortestSubArray([1,2,3,4])
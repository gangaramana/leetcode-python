from typing import List



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        no=[-1]
        # def bin(start,finish,target):
        #     middle=int((start+finish)/2)
        #     if(nums[middle]==target):
        #         return middle
        #     elif(nums[middle]>=target and target<=nums[finish]):
        #         no[0]=bin(middle,finish,target)
        #     elif(nums[middle]<=target and target <=nums[finish]):
        #         no[0]=bin(middle,finish,target)
        #     elif(nums[middle]>=target and target>=nums[start]):
        #         # no[0]=bin()
        #
        #         sa=1
        #     return no[0]
        no[0]= bin(0,len(nums)-1,target)
        return no[0]



if __name__ == '__main__':
    obj=Solution()
    x=[3,4,5,6,7,0,1,2]
    re=obj.search(x,2)
    print(re)

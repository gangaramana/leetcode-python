from typing import List
from math import  ceil
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res=[0]

        def binary_srch(nums,L,R):
            n = ceil((L + R) / 2)
            if(R-L >0):

                if(nums[n]==nums[n+1]):
                  res[0]= binary_srch(nums,L,n-1)
                elif (nums[n]==nums[n-1]):
                  res[0]=  binary_srch(nums,n+1,R)
                else:
                    return nums[n]

            else:
                return R
            return res[0]

        res[0]= binary_srch(nums, 0, len(nums)-1)
        return res[0]



if __name__=="__main__":
    obj=Solution()
    x=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,22,22,33]
    v=obj.singleNonDuplicate(x)
    print(len(x))
    print(x[v])


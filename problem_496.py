from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        l=len(nums2)
        for i in nums1:
            x=nums2.index(i)+1
            if(x<l and i<nums2[x] ):
                result.append(nums2[x])
            else:
                result.append(-1)
        return result


if __name__ == '__main__':
    obj=Solution()
    obj.nextGreaterElement([])


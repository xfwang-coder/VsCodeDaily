# remove the duplicates，return the length of nums
# 这里采用非删除的方式，首先初始化第一个元素i,比对后续元素；
#如果与之不同，则将该元素放置在nums[i+1]处，反之则忽略，继续寻找第j+1个元素
nums = [1,1,2,0,3,2]
#print(nums[0])
i = 0
#
for j in range(1,len(nums)):
    if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]
print(i+1)
"""
class Solution(object):
    def removeDuplicates(self,nums):
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1

"""

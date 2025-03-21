#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ass_set = set()

        for num in nums:
            if num not in ass_set:
                ass_set.add(num)
            else:
                return num


# @lc code=end

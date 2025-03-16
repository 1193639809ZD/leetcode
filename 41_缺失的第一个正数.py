#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode.cn/problems/first-missing-positive/description/
#
# algorithms
# Hard (46.55%)
# Likes:    2308
# Dislikes: 0
# Total Accepted:    507.7K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,0]
# 输出：3
# 解释：范围 [1,2] 中的数字都在数组中。
#
# 示例 2：
#
#
# 输入：nums = [3,4,-1,1]
# 输出：2
# 解释：1 在数组中，但 2 没有。
#
# 示例 3：
#
#
# 输入：nums = [7,8,9,11,12]
# 输出：1
# 解释：最小的正数 1 没有出现。
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    # 正常算法
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     ass_list = [0 for _ in range(n + 1)]
    #     for num in nums:
    #         if num <= 0 or num > n:
    #             continue
    #         else:
    #             ass_list[num] = 1
    #
    #     for i in range(1, n + 1):
    #         if ass_list[i] == 0:
    #             return i
    #     return n + 1

    # 利用set的性质，可以快速建立查询表
    def firstMissingPositive(self, nums: List[int]) -> int:
        ass_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in ass_set:
                return i
        return len(nums) + 1


# @lc code=end

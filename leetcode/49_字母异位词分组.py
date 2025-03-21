#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            temp = "".join(sorted(s))
            ans[temp].append(s)

        return list(ans.values())


# @lc code=end

#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        res = [False] * (n + 1)
        res[0] = True

        wordDict = set(wordDict)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if res[i] and s[i:j] in wordDict:
                    res[j] = True

        return res[-1]


# @lc code=end

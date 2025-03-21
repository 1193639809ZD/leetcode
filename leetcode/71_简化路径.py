#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = path.split("/")
        print(f"temp: {temp}")

        # 处理路径
        ans = []
        for p in temp:
            # '/' 和 '.' 直接删除
            if p == "/" or p == "." or p == "":
                continue
            elif p == "..":
                # 如果ans有值，弹出上一个路径，否则跳过
                if ans:
                    ans.pop()
                else:
                    continue
            else:
                ans.append(p)
        print(f"ans: {ans}")
        return "/" + "/".join(ans)


# @lc code=end

"""
204. 计数质数
统计所有小于非负整数 n 的质数的数量。

示例 1：
输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

示例 2：
输入：n = 0
输出：0

示例 3：
输入：n = 1
输出：0

提示：
0 <= n <= 5 * 106
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        store = [1] * n
        store[0], store[1] = 0, 0
        for i in range(2, int(n**0.5) + 1):
            if store[i]:
                for j in range(i * i, n, i):
                    store[j] = 0
        return sum(store)


if __name__ == "__main__":
    test = Solution().countPrimes(10)
    print(test)
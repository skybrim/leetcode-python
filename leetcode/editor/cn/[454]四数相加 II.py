# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[
# l] = 0。 
# 
#  为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最
# 终结果不会超过 231 - 1 。 
# 
#  例如: 
# 
#  
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# 输出:
# 2
# 
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#  
#  Related Topics 哈希表 二分查找 
#  👍 239 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sum_a_b = {}
        for i in A:
            for j in B:
                if i + j in sum_a_b:
                    sum_a_b[i + j] += 1
                else:
                    sum_a_b[i + j] = 1
        res = 0
        for k in C:
            for l in D:
                if -(k + l) in sum_a_b.keys():
                    res += sum_a_b[-(k + l)]
        return res

# leetcode submit region end(Prohibit modification and deletion)

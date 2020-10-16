"""
977. 有序数组的平方
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]

提示：
1. 1 <= A.length <= 10000
2. -10000 <= A[i] <= 10000
3. A 已按非递减顺序排序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import deque


def sorted_squares(a):
    negative = deque()
    positive = []
    for num in a:
        if num < 0:
            negative.appendleft(num * num)
        else:
            positive.append(num * num)
    if len(negative) == 0:
        return positive
    if len(positive) == 0:
        return negative
    index = 0
    for num in negative:
        while index < len(positive) and num > positive[index]:
            index += 1
        if index == len(positive):
            positive.append(num)
        else:
            positive.insert(index, num)
        index += 1
    return positive


if __name__ == '__main__':
    print(sorted_squares([-3, 0, 2]))

"""
57. 插入区间

给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例1：
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]

示例2：
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def insert(intervals, newInterval):
    result = []
    is_insert = False
    left, right = newInterval
    for cur_l, cur_r in intervals:
        if right < cur_l:
            if not is_insert:
                is_insert = True
                result.append([left, right])
            result.append([cur_l, cur_r])
        elif left > cur_r:
            result.append([cur_l, cur_r])
        else:
            left = min(cur_l, left)
            right = max(cur_r, right)
    if not is_insert:
        result.append([left, right])
    return result


if __name__ == "__main__":
    print(insert([[1, 5]], [2, 3]))

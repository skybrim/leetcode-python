"""
34. 在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

提示：
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def search_range(nums, target):
    if len(nums) == 0:
        return [-1, -1]

    left = binary_search_left(nums, target)
    if left == -1:
        return [-1, -1]
    right = binary_search_right(nums, target)
    return [left, right]


def binary_search_left(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            right = mid
        else:
            right = mid - 1
    if nums[left] == target:
        return left
    return -1


def binary_search_right(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left + 1) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            left = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    print(search_range([5, 7, 7, 8, 8, 10], 8))
"""
1002 查找常用字符

给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-common-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from collections import Counter

def commonChars_counter(A):
    tmp = Counter(A[0])
    for word in A[1:]:
        chars = Counter(word)
        tmp &= chars
    return list(tmp.elements())

def commonChars(A):
    minfreq = None

    for word in A:
        cur_freq = {}
        for char in word:
            if char not in cur_freq:
                cur_freq[char] = 1
            else:
                cur_freq[char] = cur_freq[char] + 1
        if minfreq is None:
            minfreq = cur_freq
        else:
            for key in minfreq:
                if key not in cur_freq:
                    minfreq[key] = 0
                else:
                    minfreq[key] = min(minfreq[key], cur_freq[key])

    result = []
    for key in minfreq:
        for i in range(minfreq[key]):
            result += [key]
    return result


print(commonChars(["bella", "label", "roller"]))

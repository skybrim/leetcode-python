"""
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
	int val;
	Node *left;
	Node *right;
	Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque()
        tmp_queue = deque()
        queue.append(root)
        while queue:
            for index in range(len(queue)):
                queue[index].next = queue[index + 1]
            node = queue.popleft()
            if node.left:
                tmp_queue.append(node.left)
                tmp_queue.append(node.right)
            if not queue:
                queue = tmp_queue
                tmp_queue = deque()
        return root


class Solution_2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        left_most = root
        while left_most.left:
            head = left_most
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            left_most = left_most.left
        return root


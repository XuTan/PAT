"""
1004. Counting Leaves (30)
时间限制
400 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
CHEN, Yue
A family hierarchy is usually presented by a pedigree tree. Your job is to count those family members who have no child.

Input
Each input file contains one test case. Each case starts with a line containing 0 < N < 100, the number of nodes in a tree, and M (< N), the number of non-leaf nodes. Then M lines follow, each in the format:
ID K ID[1] ID[2] ... ID[K]
where ID is a two-digit number representing a given non-leaf node, K is the number of its children, followed by a sequence of two-digit ID's of its children. For the sake of simplicity, let us fix the root ID to be 01.

Output
For each test case, you are supposed to count those family members who have no child for every seniority level starting from the root. The numbers must be printed in a line, separated by a space, and there must be no extra space at the end of each line.
The sample case represents a tree with only 2 nodes, where 01 is the root and 02 is its only child. Hence on the root 01 level, there is 0 leaf node; and on the next level, there is 1 leaf node. Then we should output "0 1" in a line.
Sample Input
2 1
01 1 02
Sample Output
0 1
"""


class Node(object):

    def __init__(self, ID, parent=None, children=None):
        self.id = ID
        self.parent = parent
        if children is None:
            self.children = []
        else:
            self.children = children

    def child_append(self, other):
        if isinstance(other, list):
            self.children += other
        else:
            self.children.append(other)


def main():
    nodes, non_leaf = [int(_) for _ in input().split()]
    if nodes == 1:
        print("1", end='')
        return

    nodes_dict = {}

    for i in range(non_leaf):
        leaf_id, children, *children_id = input().split()
        if leaf_id not in nodes_dict:
            leaf_node = Node(ID=leaf_id)
            nodes_dict[leaf_id] = leaf_node
        else:
            leaf_node = nodes_dict[leaf_id]

        for child in children_id:
            if child not in nodes_dict:
                child_node = Node(ID=child, parent=leaf_node)
                nodes_dict[child] = child_node
            else:
                child_node = nodes_dict[child]
                child_node.parent = leaf_node

            leaf_node.child_append(child_node)

    root_queue = [nodes_dict['01']]
    res = []

    def recursive(layer_queue):
        nonlocal res
        if layer_queue:
            non_leaf_num = 0
            next_queue = []
            for node in layer_queue:
                if not node.children:
                    non_leaf_num += 1
                else:
                    next_queue += node.children

            res.append(non_leaf_num)
            recursive(next_queue)

    recursive(root_queue)
    res = [str(_) for _ in res]
    print(' '.join(res), end='')


if __name__ == '__main__':
    main()

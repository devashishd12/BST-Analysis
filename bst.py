import numpy as np
from matplotlib import pyplot as plt


class NodeBst:
    """Implementation of binary search trees"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, node):
    """Inserts node at required position"""
    if node.data < root.data:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
    elif node.data > root.data:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        return root


def height(root):
    """Calculate height of tree using level order traversal
    from geeksforgeeks.com"""
    if root is None:
        return 0

    q = []
    q.append(root)
    height = 0

    while(True):
        nodeCount = len(q)
        if nodeCount == 0:
            return height
        height += 1

        while(nodeCount > 0):
            node = q[0]
            q.pop(0)
            if node.left is not None:
                q.append(node.left)
            elif node.right is not None:
                q.append(node.right)
            nodeCount -= 1


if __name__ == '__main__':
    for _ in xrange(5):
        constant = []
        root = NodeBst(5000)
        used = set()
        Height = []
        x = []
        for i in range(1, 10000, 1):
            j = np.random.randint(10000)
            if j not in used or j != 0:
                used.add(j)
                insert(root, NodeBst(j))
                Height.append(height(root))
                x.append(float(sum(Height)) / len(Height))
                constant.append(x[-1] / np.log2(i + 1))
            else:
                continue
        plt.scatter(range(len(x)), x, marker='.', linewidths=1e-6, color='r',
                    label='E[x{0}]'.format(_))

    print (float(sum(constant)) / len(constant))

    plt.plot(range(1, 10000, 1), np.log2(range(1, 10000, 1)), color='b',
             label='log(n)')
    plt.legend(loc='lower right')
    plt.ylim(ymin=0)
    plt.show()

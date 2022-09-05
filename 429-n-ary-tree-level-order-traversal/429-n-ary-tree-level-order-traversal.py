"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def traverse(root, level):
            if not root: return
            while len(ret) <= level:
                ret.append([])

            ret[level].append(root.val)
            for child in root.children:
                traverse(child, level + 1)

        ret = []
        traverse(root, 0)
        return ret
        
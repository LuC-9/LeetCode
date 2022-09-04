# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root, 0)]
        node_map = dict()
        while stack:
            tmp = dict()
            for _ in range(len(stack)):
                node, index = stack.pop(0)
                if node:
                    tmp[index] = tmp.get(index, []) + [node.val]
                if node.left: stack.append((node.left, index - 1))
                if node.right: stack.append((node.right, index + 1))

            tmp = {k: sorted(i) for k, i in tmp.items()}
            node_map = {k: node_map.get(k, []) + tmp.get(k, []) for k in list(tmp.keys()) + list(node_map.keys())}
        res = sorted([(index, val) for index, val in node_map.items()], key=lambda x: x[0])
        return [i for _, i in res]
        
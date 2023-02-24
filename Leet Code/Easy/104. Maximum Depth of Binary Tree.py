# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        null = None
        if root == None : return 0
        if  str(type(root)) != "<class 'precompiled.treenode.TreeNode'>": return 1
        level = 1
        tree = [[root]]
        while True:
            g = []
            is_there_node = False
            for i in tree[level-1]:
                if str(type(i.left)) == "<class 'precompiled.treenode.TreeNode'>":
                    is_there_node = True
                    g.append(i.left)
                if str(type(i.right)) == "<class 'precompiled.treenode.TreeNode'>":
                    is_there_node = True
                    g.append(i.right)
            if not is_there_node:
                break
            level +=1
            tree.append(g)
        return level
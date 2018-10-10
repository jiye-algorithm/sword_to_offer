'''
给定一颗二叉树，变成一个链表

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.prev = None
        pass

    def flatten(self, root):
        '''
        利用后续遍历的方式，
        对于当前节点，右子树就是刚才访问的节点，左子树就是None， 然后刚才访问的节点置为当前节点
        子下而上构建
        '''
        if not root:
            return None
        # 右子树
        self.flatten(root.right)
        # 左子树
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
        pass

    pass

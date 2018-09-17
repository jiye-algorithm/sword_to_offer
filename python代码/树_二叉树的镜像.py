'''操作给定的二叉树，将其变换为源二叉树的镜像。'''# -*- coding:utf-8 -*-class TreeNode:    def __init__(self, x):        self.val = x        self.left = None        self.right = None        passclass Solution:    # 返回镜像树的根节点    def Mirror(self, root):        # 知道根节点为空        if root != None:            # 镜像根节点的            root.left, root.right = root.right, root.left            # 镜像左子树            self.Mirror(root.left)            # 镜像右子树            self.Mirror(root.right)        pass    pass
'''
请实现两个函数，分别用来序列化和反序列化二叉树


1. 对于序列化：使用前序遍历，递归的将二叉树的值转化为字符，并且在每次二叉树的结点
不为空时，在转化val所得的字符之后添加一个' ， '作为分割。对于空节点则以 '#' 代替。
 2. 对于反序列化：按照前序顺序，递归的使用字符串中的字符创建一个二叉树(特别注意：
在递归时，递归函数的参数一定要是char ** ，这样才能保证每次递归后指向字符串的指针会
随着递归的进行而移动！！！)


"{8,6,10,5,7,9,11}"
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 这里从 -1开始方便开始+1
    flag = -1

    def Serialize(self, root):
        return self.recursionSerialize(root)

    def recursionSerialize(self, root):
        # 空节点用 $ 代替
        if root is None:
            return '$,'

        # 序列化该节点
        s = str(root.val) + ','
        # 序列化左子树
        left = self.recursionSerialize(root.left)
        # 序列化右子树
        right = self.recursionSerialize(root.right)
        # 该树的序列化结果
        s += left + right
        return s

    def Deserialize(self, s):
        # 全局变量，用来保存在数组中第几个访问的元素
        self.flag += 1
        l = s.split(',')
        # 访问的数量必须少于字符串的长度
        if (self.flag >= len(s)):
            return None

        root = None
        # 如果当前字符不是空字符
        if (l[self.flag] != '$'):
            # 父节点
            root = TreeNode(int(l[self.flag]))
            # 左子树
            root.left = self.Deserialize(s)
            # 右子树
            root.right = self.Deserialize(s)
        # 根节点
        return root


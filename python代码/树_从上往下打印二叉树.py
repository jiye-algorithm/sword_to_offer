'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

def PrintFromTopToBottom(self, root):
        if not root:
            return []
        # 辅助队列
        currentStack = [root]
        # 保存结果队列
        res = []
        while currentStack:
            nextStack = []
            for i in currentStack:
                # 左子树加入
                if i.left: nextStack.append(i.left)
                # 右子树加入
                if i.right: nextStack.append(i.right)
                res.append(i.val)
            currentStack = nextStack
        return res
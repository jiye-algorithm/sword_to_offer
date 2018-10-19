'''
https://leetcode.com/problems/generate-random-point-in-a-circle/


题目大意
给定圆的圆心和半径，生成落在这个圆里面的随机点。

解题方法
比较简单的方法是拒绝采样（Rejection Sampling），先在圆的外接圆内随机采点，然后判断这个点是不是在圆内，如果是的话就返回，否则再取一次。这个方法还可以用来估计圆周率。方法就不写了。。

我直觉的方法还是使用极坐标的方式，随机找半径、随机找角度，然后就确定了一个点。但是没有通过最后一个测试用例。如果不查资料我是不会发现，这个做法是错的……

直接对半径和角度进行随机采样的方式会使得靠近圆心的点被取到的概率偏大，而在这个圆内不是均匀的。为什么呢？因为题目要求的是对圆内任何面积上的点是均匀分布的，而不是对圆心出发的线上是均匀分布的。那么以圆心为半径的小圆的范围内的点密度一定会比更大圆的密度大。




https://blog.csdn.net/fuxuemingzhu/article/details/83051190


'''

'''
小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。
你知道了小易对一堂课每分钟知识点的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，你可以叫醒他一次，
这会使得他在接下来的k分钟内保持清醒。你需要选择一种方案最大化小易这堂课听到的知识点分值。 

输入描述:
第一行 n, k (1 <= n, k <= 105) ，表示这堂课持续多少分钟，以及叫醒小易一次使他能够保持清醒的时间。
第二行 n 个数，a1, a2, ... , an(1 <= ai <= 104) 表示小易对每分钟知识点的感兴趣评分。
第三行 n 个数，t1, t2, ... , tn 表示每分钟小易是否清醒, 1表示清醒。


输出描述:
小易这堂课听到的知识点的最大兴趣值。

输入例子1:
6 3
1 3 5 2 5 4
1 1 0 1 0 0

输出例子1:
16
'''
'''
思路：从左到右遍历，比较k长度内睡着0状态对应兴趣值的和，即叫醒一下提升的兴趣值。
    总值分为两部分：醒着的固定值 + 睡着的提升值的最大值
'''
def max_interest_value(n, k):
    # 每分钟感兴趣权值
    interest_value = [int(i) for i in input().strip().split()]
    # 每分钟是不是清醒
    awake = [int(i) for i in input().strip().split()]
    base_scope = 0
    # 计算所有的清醒时刻
    for i in range(n):
        if awake[i] == 1:
            base_scope += interest_value[i]
            interest_value[i] = 0
    # 对于没有清醒时刻，叫醒后得到的分数
    max_boost_value = 0
    for i in range(n):
        if awake[i] == 0:
            boost_value = sum(interest_value[i : min(i + k, n)])
            max_boost_value = max(boost_value, max_boost_value)
            # 加了下面的break语句，才使这个代码时间上终于达标
            # 扫描到距结尾不足k距离范围内的第一个睡着状态即可，后面的肯定不如这个的提升值大，没必要再跑，可提前结束
            # 注意： 这里和直接使用 range(n - k + 2)不一样，这里其实是两个条件：<n 并且 < n - k + 1
            if i > n - k + 1:
                break
    return base_scope + max_boost_value


n, k = map(int, input().strip().split())

print(max_interest_value(n, k))
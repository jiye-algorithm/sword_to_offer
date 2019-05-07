'''
你从0开始走到 target 
step从1 开始， 每次可以走往左或者往右走step不，最小的移动步数 

input： 3
output = 2
解释： 
    第一次： 0 -- 1
    第二次： 1 -- 3
    
input： 2
output = 3
解释： 
    第一次： 0 -- 1
    第二次： 1 -- -1
    第三次： -1 -- 2
'''

target = int(input().strip())

step = 1
target = target if target > 0 else -target
num = 0
while num + step != target:
    if num + step < target:
        num += step
    else:
        num -= step
    step += 1
    pass

print(step)
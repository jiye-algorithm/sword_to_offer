'''
给定一个表达式字符串， 仅包含+-*/和数字，不包含任何其他字符，规定加减优先级高于乘除，
输出该表达式的值，

输入 1+2*3  输出  9
输入：1-8/3+1  输出-1

输入描述
    每一行是一个字符串形式的表达式，以换行结束

输出描述：
    输出对应的计算结果，用一个整数表示
    
示例1
    输入
        1+6/3
    输出
        2
'''


line = input()
# line = "1-8/3+1"
fuhao = ("+","-","*","/")
def yunsuan(a,b,c):
    if c == "+":
        return a+b
    if c == "-":
        return b-a
    if c == "*":
        return a*b
    if c == "/":
        return b/a

fuzhan = ["#"]
shuzhan = []
all = int(line[0])
for i in line:
    if i in fuhao:
        if ((i == "*" or i == "/") and fuzhan[-1] !="#") or ((i == "+" or i == "-") and (fuzhan[-1]== "+" or fuzhan[-1]== "-")):

            yusuan = fuzhan.pop()
            all= yunsuan(float(shuzhan.pop()),float(shuzhan.pop()),yusuan)
            fuzhan.append(i)
            shuzhan.append(all)
        else:
            fuzhan.append(i)
    else:
        shuzhan.append(i)

while fuzhan[-1] != "#":
    all= yunsuan(float(shuzhan.pop()),float(shuzhan.pop()),fuzhan.pop())
    shuzhan.append(all)
print(int(all))
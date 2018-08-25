line ={}
chaxun_=[]
n,m = map(int,input().split(" "))
for i in range(n):
    li = input().split(" ")
    line[li[0]] = [int(li[2]),-1,li[4]]
for index in range(m):
    chaxun_.append(input().split(" "))

for key in list(line.keys()):
    if line.get(line[key][-1],0) ==0:
        not_move = line[key][-1]
        dont_move_key = key
for i in range(len(line)):
    for key in line:
        if line[key][-1] == dont_move_key :
            line[key] = [line[key][0] - line[dont_move_key][0], line[key][1] *line[key][1],line[dont_move_key][-1]]
            dont_move_key = key
for chaxun in chaxun_:
    if chaxun[2] == not_move:
        ll = 0
        kk = 1
    else:
        ll =  line[chaxun[2]][0]
        kk =  line[chaxun[2]][1]
    if chaxun[0] == not_move:
        l2 = 0
        k2 = 1
    else:
        l2 = line[chaxun[0]][0]
        k2 = line[chaxun[0]][1]
    result = l2 -  ll
    if (k2 * kk)<0 :
      print('cannot_answer')
    else:
      print(result)






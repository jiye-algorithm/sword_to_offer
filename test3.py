def solve(vlist,wlist,totalWeight,totalLength):
    resArr = [[0 for i in range(totalWeight+1)] for _ in range(totalLength+1)]
    for i in range(1,totalLength+1):
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[i][j] = max(resArr[i-1][j - wlist[i]] + vlist[i], resArr[i-1][j])
            else:
                resArr[i][j] = resArr[i-1][j]
    return resArr[-1][-1]

if __name__ == '__main__':
    v = [0,60,100,120]
    w = [0,10,20,30]
    weight = 50
    n = 3
    result = solve(v,w,weight,n)
    print(result)
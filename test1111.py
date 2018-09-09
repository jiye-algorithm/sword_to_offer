N, M = list(map(int, input().strip().split()))[0: 2]

graph = [] * N
color = [] * N

for i in range(M):
    start, end = list(map(int, input().strip().split()))[0: 2]
    graph[start].append(end)


def dfs(v, c):

    color[v] = c

    for i in range(len(graph[v])):
        if(color[graph[v][i]] == c):
            return False
        if(color[graph[v][i]] == 0 and not dfs(graph[v][i], -c)) :
            return False

    return True

def solve():
    for i in range(N):
        if(color[i] == 0):
            if(not dfs(i, 1)):
                print("No")
                return


solve()

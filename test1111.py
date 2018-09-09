M = int(input().strip())
input_matrix = []
for _ in range(M):
    input_matrix.append(list(map(int, input().strip().split())))

flag = [[0] * M for i in range(M)]
def find(matrix, i, j, flag):
    if 0<= i < M and 0<= j < M:
        if matrix[i][j] and not flag[i][j]:
            flag[i][j] = True
            find(matrix, i-1, j, flag)
            find(matrix, i+1, j, flag)
            find(matrix, i, j-1, flag)
            find(matrix, i, j+1, flag)
            return True
    return False

count = 0
for i in range(M):
    for j in range(M):
        if find(input_matrix, i, j, flag):
            count += 1
print(count)


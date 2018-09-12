import heapq


def GetLeastNumbers_Solution(tinput, k):
    if len(tinput) < k:
        return []
    return heapq.nlargest(k, tinput)


# 2,4,2,7,7-3,2,5,6,1,9:6
my_input = input().strip()
my_input_1, my_input_2 = my_input.split('-')
my_input_2 = my_input_2.split(":")[0]

arr_1 = list(map(int, my_input_1.split(',')))
arr_2 = list(map(int, my_input_2.split(',')))
k = int(my_input.strip().split(":")[-1])

my_sum = []
for i in arr_1:
    for j in arr_2:
        my_sum.append(i + j)

print(GetLeastNumbers_Solution(my_sum, k))


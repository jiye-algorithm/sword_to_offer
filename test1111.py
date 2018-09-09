N = int(input().strip())
M = int(input().strip())

my_input = list(map(int, input().strip().split()))

i = 0
my_map = {}
for i in set(my_input):
    my_map[i] = []

while i < len(my_input):
    start, end = my_input[i : i + 2]
    my_map[end].append(start)
    for it in my_map[start]:
        my_map[end].append(it)
    my_map[end] = set(my_map[end])
    
for key, value in my_map.items():
    if len(my_map[key]) == len(my_map):
        print(key)
        break
    


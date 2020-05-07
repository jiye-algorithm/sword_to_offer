my_input = input().strip()

my_dict ={}
for i in my_input:
    my_dict[i] = my_dict.get(i, 0) + 1

my_keys = sorted(my_dict.keys())

ans = ""
for i in range(len(my_dict)):
    ans += str(my_keys[i])
    ans += str(my_dict[my_keys[i]])

print(ans)
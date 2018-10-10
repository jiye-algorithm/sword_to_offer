n, m = [int(x) for x in input().strip().split()]

trees = [int(x) for x in input().strip().split()]
trees = list(reversed(sorted(trees)))

i, h = 0, 0
#print(trees)
while m > 0 and i < len(trees) - 1:
    m -= (trees[i] - trees[i+1]) * (i + 1)
    h += trees[i] - trees[i+1]
    #print(m, h)
    i += 1

if m < 0:
    h -= (-m) // i

print(trees[0] - h)

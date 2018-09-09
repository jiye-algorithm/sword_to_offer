line = input().strip()

left = 0
right = 0
ans = 0
visited = [0] * 256 
while left < len(line):
    if right < len(line) and visited[ord(line[right])] == 0:
        visited[ord(line[right])] += 1
        right += 1
    else:
        visited[ord(line[left])] -= 1
        left += 1

    asn = max(ans, right - left)

print(ans)


    
    

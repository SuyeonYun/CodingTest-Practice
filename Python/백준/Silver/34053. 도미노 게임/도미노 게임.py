n, m = map(int, input().split())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))

        
total_sum = 0
total_min = min(info[0])
for i in range(n):
    total_sum += sum(info[i])
    if min(info[i]) < total_min:
        total_min = min(info[i])
        
        
if total_min == 0:
    print(total_sum)
else:
    print(total_sum - total_min)
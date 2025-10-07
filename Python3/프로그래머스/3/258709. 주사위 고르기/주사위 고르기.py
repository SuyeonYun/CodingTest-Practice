import itertools

def lower(l, target):
    left, right = 0, len(l)
    while left < right:
        mid = (left + right) // 2
        if l[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
    
def upper(l, target):
    left, right = 0, len(l)
    while left < right:
        mid = (left + right) // 2
        if l[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def solution(dice):
    n = len(dice)
    arr = []
    result = []
    groups = []
    
    for group in itertools.combinations([i for i in range(n)], int(n/2)):
        group = list(group)
        groups.append([x + 1 for x in group])
        arr.append([])
        result.append(0)
        
        for a in range(6):
            if n == 2:
                arr[-1].append(dice[group[0]][a])
            for b in range(6):
                if n == 4:
                    arr[-1].append(dice[group[0]][a] + dice[group[1]][b])
                for c in range(6):
                    if n == 6:
                        arr[-1].append(dice[group[0]][a] + dice[group[1]][b] + dice[group[2]][c])
                    for d in range(6):
                        if n == 8:
                            arr[-1].append(dice[group[0]][a] + dice[group[1]][b] + dice[group[2]][c] + dice[group[3]][d])
                        for e in range(6):
                            if n == 10:
                                arr[-1].append(dice[group[0]][a] + dice[group[1]][b] + dice[group[2]][c] + dice[group[3]][d] + dice[group[4]][e])

        
    for i in range(len(arr)):
        arr[i].sort()
        
    arr_n = len(arr)
    arri_n = len(arr[0])
    for i in range(int(arr_n / 2)):
        for j in range(arri_n):
            lower_bound = lower(arr[arr_n - i - 1], arr[i][j])
            upper_bound = upper(arr[arr_n - i - 1], arr[i][j])
            
            result[arr_n - i - 1] += arri_n - upper_bound
            result[i] += lower_bound
    
    max_n = 0
    max_i = 0
    for i in range(arr_n):
        if max_n < result[i]:
            max_n = result[i]
            max_i = i
    
    return groups[max_i]
            
def solution(numbers):
    numbers.sort(key = lambda num : str(num)*3 , reverse = True)
    answer = str(int(''.join(str(n) for n in numbers)))
    return answer
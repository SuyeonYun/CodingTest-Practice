import itertools as it

def is_prime(number):
    if number < 2 : 
        return False
    for i in range(3, number):
        if number % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i,j,k in it.combinations(nums, 3) :
        if is_prime(i+j+k) :
            answer += 1
    return answer
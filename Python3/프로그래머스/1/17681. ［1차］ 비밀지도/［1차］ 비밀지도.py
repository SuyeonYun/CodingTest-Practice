def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        binary = bin(arr1[i] | arr2[i])[2:].zfill(n)

        line = ''.join('#' if ch == '1' else ' ' for ch in binary)
        answer.append(line)

    return answer
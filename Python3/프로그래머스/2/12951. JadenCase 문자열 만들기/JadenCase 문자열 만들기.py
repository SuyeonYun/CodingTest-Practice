def solution(s):
    return ' '.join([f"{str[0].upper()}{str[1:].lower()}" if len(str) >= 1 else str for str in s.split(" ")])
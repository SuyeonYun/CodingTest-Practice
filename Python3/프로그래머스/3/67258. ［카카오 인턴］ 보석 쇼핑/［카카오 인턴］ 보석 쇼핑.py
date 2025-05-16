from collections import defaultdict

def solution(gems):
    # 전체 보석 종류 수
    unique_total = len(set(gems))
    counts = defaultdict(int)
    answer = [1, len(gems)]  # 최댓값으로 초기화
    start = 0
    
    for end, gem in enumerate(gems):
        counts[gem] += 1
        # 현재 윈도우에 모든 종류가 포함되면 start를 이동시키며 최소 구간 찾기
        if len(counts) == unique_total:
            while start < end:
                if counts[gems[start]] > 1:
                    counts[gems[start]] -= 1
                    start += 1
                else:
                    break
            # 구간이 더 짧으면 갱신
            if end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1]
    return answer
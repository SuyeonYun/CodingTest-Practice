from dataclasses import dataclass
from collections import deque
import heapq
from typing import List, Tuple

@dataclass
class Job:
    """디스크 작업을 나타내는 클래스"""
    id: int
    request_time: int
    duration: int
    start_time: int = None
    end_time: int = None

    @property
    def turnaround_time(self) -> int:
        """작업의 총 소요시간 (종료시간 - 요청시간)"""
        return self.end_time - self.request_time if self.end_time else 0

    def __lt__(self, other: 'Job') -> bool:
        """작업 우선순위 비교: 소요시간 > 요청시간 > 작업ID 순"""
        return (
            (self.duration, self.request_time, self.id) < 
            (other.duration, other.request_time, other.id)
        )

def solution(jobs: List[Tuple[int, int]]) -> int:
    """디스크 작업의 평균 처리시간을 계산"""
    # 작업 초기화
    total_jobs = len(jobs)
    job_queue = deque(sorted(
        [Job(i, req_time, duration) 
         for i, (req_time, duration) in enumerate(jobs)],
        key=lambda x: x.request_time
    ))

    waiting_queue = []
    completed_jobs = []
    current_job = None
    current_time = 0

    # 모든 작업이 완료될 때까지 처리
    while len(completed_jobs) < total_jobs:
        # 현재 시간에 도착한 작업들을 대기열에 추가
        while job_queue and job_queue[0].request_time == current_time:
            heapq.heappush(waiting_queue, job_queue.popleft())

        # 현재 작업이 완료되었거나 없는 경우
        if (not current_job or 
            current_job.start_time + current_job.duration == current_time):

            # 현재 작업 완료 처리
            if current_job:
                current_job.end_time = current_time
                completed_jobs.append(current_job)

            # 새 작업 할당
            if waiting_queue:
                current_job = heapq.heappop(waiting_queue)
                current_job.start_time = current_time
            else:
                current_job = None

        current_time += 1

    # 평균 처리시간 계산
    total_turnaround_time = sum(job.turnaround_time for job in completed_jobs)
    return total_turnaround_time // total_jobs
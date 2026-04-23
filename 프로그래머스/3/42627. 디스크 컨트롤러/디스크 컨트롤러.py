import heapq

def solution(jobs):
    jobs.sort()  # 요청 시각 기준 정렬
    jobs = sorted(jobs, key = lambda x:(x[0],x[1]))
    
    heap = []
    time = 0
    i = 0
    total = 0
    n = len(jobs)

    while i < n or heap:
        # 현재 시각까지 들어온 작업 넣기
        while i < n and jobs[i][0] <= time:
            req, dur = jobs[i]
            heapq.heappush(heap, (dur, req, i))  # 소요시간, 요청시각, 번호
            i += 1

        if heap:
            dur, req, idx = heapq.heappop(heap)
            time += dur
            total += time - req
        else:
            # 대기 작업이 없으면 다음 요청 시각으로 이동
            time = jobs[i][0]

    return total // n
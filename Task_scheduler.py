from collections import Counter
import heapq

def leastInterval(task,n):
    if n == 0:
        return len(task)

    task_count = Counter(task)
    task_heap = [-count for count in task_count.values()]
    heapq.heapify(task_heap)

    total_time = 0

    while task_heap:
        cycle = []
        for _ in range(n+1):
            if task_heap:
                cycle.append(heapq.heappop(task_heap))

        for task in cycle:
            if task + 1 < 0:
                heapq.heappush(task_heap, task+1)

        total_time += len(task_heap) and n + 1 or len(cycle)

    return total_time

def test_leastInterval():
    assert leastInterval(["A","A","A","B","B","B"], 2) == 8
    assert leastInterval(["A","A","A","B","B","B"], 0) == 6
    assert leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) == 16
    print("Todos os testes passaram.")

test_leastInterval()
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        prev_task_day = {}
        ans = 0
        for i, task in enumerate(tasks):
            ans += 1
            if task in prev_task_day:
                if ans - prev_task_day[task] <= space:
                    ans += space - (ans - prev_task_day[task]) + 1
            prev_task_day[task] = ans
        return ans
            
        
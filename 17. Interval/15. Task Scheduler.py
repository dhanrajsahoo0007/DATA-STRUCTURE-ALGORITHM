"""
Initialize a frequency map using Counter to count how often each task appears.
Set up a max heap, a deque (for cooldown tracking), and a timer.
Add all tasks from the frequency map to the max heap, storing their negative frequencies (to get the max heap).
While there are tasks left in either the heap or the cooldown queue:
Pop the task with the highest frequency from the heap. If it has remaining executions, add it to the cooldown queue with its next available time (timer + n + 1), and decrement its execution count.
Increment the timer by 1. This has to be done outside of both heap and queue loops, because if the heap is empty (no ready tasks to be executed) but the queue contains items that cannot be popped (because the tasks are still cooling), the timer still has to increase as this represents idle time.
Check the cooldown queue for any tasks whose cooldown has expired (i.e., timer == next available time). If so, move the task from the cooldown queue back into the heap. Only one task from the cooldown queue will be ready to return to the heap at each time interval because we are processing the tasks one interval at a time.
Once both the heap and the cooldown queue are empty, all tasks have been completed, and the timer is returned.
Complexity
Time complexity:
Main while loop:
The number of iterations the loop runs is equal to the total time required to finish all tasks (including idle times). Hence, O(timer)
Operations inside the loop:
Heap: pop/push operations = O(logk), where k is the length of heap.
Queue operations are O(1)
Counter: O(m), where m is the number of tasks
Overall: O(timer*logk) as the dominant time complexity.

Space complexity:
Overall, space complexity is O(n), where n is the number of unique tasks.

Counter: Uses O(n) space to store the frequency of each unique task.
Max Heap: Can hold up to n unique tasks, so its space complexity is O(n).
Cooldown Queue: Similarly, the cooldown queue can hold up to n unique tasks, so it also uses O(n) space.

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        One key observation is that tasks with higher frequencies should be prioritized
         because delaying them would increase idle times unnecessarily.
        By using a max heap, we ensure that tasks with the highest frequencies
         are executed as soon as possible when they are allowed, thus minimizing the chance of idle time.

        Sort the tasks based on their frequency count.
        Max heap that keeps track of all the available tasks,
         with the task of the highest frequency (the most "urgent" task) being popped first.
        Cooldown queue - this stores tasks that are in their cooldown phase
         and can’t be executed until a certain number of time intervals (n) have passed.
         The cooldown queue is a deque where each task is stored as a 
         tuple of: (remaining executions, next available time). 
         The next available time is when the task can be added back to the heap for execution.
        A global timer. Every time step (whether a task is executed or idle time occurs).
        """
        min_cpu_intervals = 0
        from collections import Counter, deque
        import heapq

        # calculate the task frequency counter
        task_freq_counter = Counter(tasks)

        heap = []
        cooldown = deque()
        timer = 0

        # max heap
        for key, val in task_freq_counter.items():
            heapq.heappush(heap, -val)
        
        while heap or cooldown:
            if heap:
                task = -heapq.heappop(heap)
                if task > 1:
                    cooldown.append((task-1, timer+n+1))
            timer += 1
            while cooldown and cooldown[0][1] == timer:
                task_count, next_iteration = cooldown[0]
                cooldown.popleft()
                heapq.heappush(heap, -task_count)
        return timer


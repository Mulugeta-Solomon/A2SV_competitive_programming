class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        processorTime.sort()
        tasks.sort(reverse=True)
        min_time = float('-inf')
        processor_index = 0

        for proce_time in processorTime:
            current_max = 0
            count = 0

            while processor_index < len(tasks) and count < 4:
                current_max = max(current_max, proce_time + tasks[processor_index])
                processor_index += 1
                count += 1

            min_time = max(min_time, current_max)
        
        return min_time
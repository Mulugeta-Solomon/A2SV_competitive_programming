class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freqs  = Counter(tasks)
        freqs = sorted(freqs.values(), reverse = True)

        max_freq = freqs[0]
        idle_time = (max_freq - 1) * n

        for freq in freqs[1:]:
            idle_time -= min(max_freq - 1, freq)
        
        idle_time = max(0, idle_time)

        return len(tasks) + idle_time
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)

        max_frequency = max(frequencies.values())

        max_frequency_tasks = sum(
            frequency == max_frequency
            for frequency in frequencies.values()
        )

        cooldown_schedule = (
            (max_frequency - 1) * (n + 1)
            + max_frequency_tasks
        )

        return max(len(tasks), cooldown_schedule)
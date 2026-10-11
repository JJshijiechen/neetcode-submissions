class LogSystem:

    def __init__(self):
        self.logs = []
        # 各粒度对应的字符串切片截取长度
        # 2017:01:01:23:59:59
        # Year:   4  ("2017")
        # Month:  7  ("2017:01")
        # Day:    10 ("2017:01:01")
        # Hour:   13 ("2017:01:01:23")
        # Minute: 16 ("2017:01:01:23:59")
        # Second: 19 ("2017:01:01:23:59:59")
        self.indices = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
        idx = self.indices[granularity]
        # 截取到指定粒度前缀进行闭区间比较
        s = start[:idx]
        e = end[:idx]
        
        return [
            log_id 
            for log_id, ts in self.logs 
            if s <= ts[:idx] <= e
        ]
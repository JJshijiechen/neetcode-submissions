class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        st = list(map(int, timestamp.split(":")))
        self.logs.append((self.convert(st), id))

    def convert(self, st):
        st[1] -= 1 if st[1] != 0 else 0
        st[2] -= 1 if st[2] != 0 else 0

        return ((st[0] - 1999) * (31 * 12) * 24 * 60 * 60 +
                st[1] * 31 * 24 * 60 * 60 +
                st[2] * 24 * 60 * 60 +
                st[3] * 60 * 60 +
                st[4] * 60 +
                st[5])

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        res = []
        s = self.granularity(start, granularity, False)
        e = self.granularity(end, granularity, True)

        for val, id in self.logs:
            if s <= val < e:
                res.append(id)

        return res

    def granularity(self, s, gra, end):
        h = {
            "Year": 0, "Month": 1, "Day": 2,
            "Hour": 3, "Minute": 4, "Second": 5
        }

        res = [1999, 0, 0, 0, 0, 0]
        st = list(map(int, s.split(":")))

        for i in range(h[gra] + 1):
            res[i] = st[i]

        if end:
            res[h[gra]] += 1

        return self.convert(res)



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)

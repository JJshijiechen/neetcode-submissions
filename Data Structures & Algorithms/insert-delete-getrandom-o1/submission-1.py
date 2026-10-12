class RandomizedSet:

    def __init__(self):
        self.numIdx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.numIdx:
            return False
        self.numIdx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numIdx:
            return False
        idx = self.numIdx[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.numIdx[last] = idx
        self.nums.pop()
        del self.numIdx[val]
        return True
        

    def getRandom(self) -> int:
        random_idx = int(random.random() * len(self.nums))
        return self.nums[random_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
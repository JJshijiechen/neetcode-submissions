class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        idx = self.numMap[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.numMap[last] = idx
        self.nums.pop()
        del self.numMap[val]
        return True

    def getRandom(self) -> int:
        random_index = int(random.random() * len(self.nums))
        return self.nums[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
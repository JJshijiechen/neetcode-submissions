class HitCounter:

  def __init__(self):
    self.times = [0] * 300
    self.hits = [0] * 300

  def hit(self, timestamp: int) -> None:
    idx = timestamp % 300
    if self.times[idx] != timestamp:
      self.times[idx] = timestamp
      self.hits[idx] = 1
    else:
      self.hits[idx] += 1

  def getHits(self, timestamp: int) -> int:
    total = 0
    for i in range(300):
      if timestamp - self.times[i] < 300:
        total += self.hits[i]
    return total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

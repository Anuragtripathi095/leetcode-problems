import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        not_present = len(self.idx[val]) == 0

        self.nums.append(val)
        self.idx[val].add(len(self.nums) - 1)

        return not_present

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False

        remove_idx = self.idx[val].pop()
        last_val = self.nums[-1]

        if remove_idx != len(self.nums) - 1:
            self.nums[remove_idx] = last_val

            self.idx[last_val].remove(len(self.nums) - 1)
            self.idx[last_val].add(remove_idx)

        self.nums.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
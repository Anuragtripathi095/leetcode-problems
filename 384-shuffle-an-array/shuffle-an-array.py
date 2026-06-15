import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]

    def reset(self) -> List[int]:
        return self.original[:]

    def shuffle(self) -> List[int]:
        arr = self.original[:]

        for i in range(len(arr)):
            j = random.randint(i, len(arr) - 1)
            arr[i], arr[j] = arr[j], arr[i]

        return arr
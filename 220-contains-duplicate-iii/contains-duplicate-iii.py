class Solution:
    def containsNearbyAlmostDuplicate(
        self,
        nums: List[int],
        indexDiff: int,
        valueDiff: int
    ) -> bool:

        if valueDiff < 0:
            return False

        buckets = {}
        width = valueDiff + 1

        for i, num in enumerate(nums):
            bucket = num // width

            # Same bucket
            if bucket in buckets:
                return True

            # Adjacent buckets
            if (bucket - 1 in buckets and
                abs(num - buckets[bucket - 1]) <= valueDiff):
                return True

            if (bucket + 1 in buckets and
                abs(num - buckets[bucket + 1]) <= valueDiff):
                return True

            buckets[bucket] = num

            # Remove elements outside sliding window
            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // width
                del buckets[old_bucket]

        return False
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        result = []
        heap = [(0, float('inf'))]  # (-height, right)
        prev_height = 0

        for x, neg_h, right in events:

            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_h:
                heapq.heappush(heap, (neg_h, right))

            curr_height = -heap[0][0]

            if curr_height != prev_height:
                result.append([x, curr_height])
                prev_height = curr_height

        return result
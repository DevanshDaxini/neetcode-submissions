class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #heap a min max heap.
        #start with the top compare the values on the left and right and check to see which one is bigger.
        #smash the two stones together according to how it is supposed to be done

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
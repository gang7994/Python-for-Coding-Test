import heapq
n = int(input())
heap = []
result = 0
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

while len(heap) != 1:
    plus_1 = heapq.heappop(heap)
    plus_2 = heapq.heappop(heap)
    heapq.heappush(heap,(plus_1 + plus_2) )
    result += (plus_1 + plus_2)

print(result)
    
    
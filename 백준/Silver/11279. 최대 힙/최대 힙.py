import sys

l = int(sys.stdin.readline())
heap = [0]

def createHeap(heap, n):
    heap.extend([n])
    i = len(heap)-1
    while i > 1:
        if n < heap[i//2]:
            break
        heap[i] = heap[i//2]
        i //= 2
    heap[i] = n
    
def deleteHeap(heap):
    if len(heap) == 1:
        return 0
    item = heap[1]
    temp = heap[len(heap)-1]
    if len(heap) > 2:
        i = 1
        j = 2
        while j <= len(heap)-1:
            if j < len(heap)-1:
                if heap[j] < heap[j+1]:
                    j += 1
            if temp >= heap[j]:
                break
            heap[i] = heap[j]
            i = j
            j *= 2
        heap[i] = temp
    heap.pop()
    
    return item
    

for _ in range(l):
    n = int(sys.stdin.readline())
    if n == 0:
        print(deleteHeap(heap))
    else:
        createHeap(heap,n)
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

ans = deque([])
count = 0

class queueMgmt:
    def __init__(self, num = 0):
        self.queue = deque([i for i in range(1, num + 1)])

    def dequeue(self):
        return self.queue.popleft()

    def enqueue(self, data):
        self.queue.append(data)

    def size(self):
        return len(self.queue)

    def rotate(self, data):
        self.queue.rotate(data)

q = queueMgmt(n)

while q.size() > 0:

    q.rotate(-k + 1)
    
    ans.append(q.dequeue())


print('<', end = '')
for i in ans:
    if i == ans[0]:
        print(f'{i}', end = '')
    else:
        print(f', {i}', end = '')

print('>')

#시간초과 해결됨
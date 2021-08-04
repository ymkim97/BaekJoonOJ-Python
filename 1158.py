import sys

n, k = map(int, sys.stdin.readline().split())

ans = []
count = 0

class queueMgmt:
    def __init__(self, num = 0):
        self.queue = [i for i in range(1, num + 1)]

    def dequeue(self):
        return self.queue.pop(0)

    def enqueue(self, data):
        self.queue.append(data)

    def size(self):
        return len(self.queue)

q = queueMgmt(n)

while q.size() > 0:

    count += 1
    if count == k:
        count = 0
        ans.append(q.dequeue())
        continue

    q.enqueue(q.dequeue())


print('<', end = '')
for i in ans:
    if i == ans[0]:
        print(f'{i}', end = '')
    else:
        print(f', {i}', end = '')

print('>')

#시간초과 해결해야함
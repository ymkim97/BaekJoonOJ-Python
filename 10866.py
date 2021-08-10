import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

class dequeMgmt:

    def __init__(self):
        self.ddeque = deque()
        self.no = 0

    def push_f(self, data):
        self.ddeque.appendleft(data)
        self.no += 1

    def push_b(self, data):
        self.ddeque.append(data)
        self.no += 1

    def pop_f(self):
        if self.is_Empty():
            print('-1')
            return
        
        print(self.ddeque.popleft())
        self.no -= 1

    def pop_b(self):
        if self.is_Empty():
            print(-1)
            return
        
        print(self.ddeque.pop())
        self.no -= 1

    def is_Empty(self):
        if self.no <= 0:
            return True
        else:
            return False

    def print_f(self):
        if self.is_Empty():
            print(-1)
            return
        print(self.ddeque[0])
    
    def print_b(self):
        if self.is_Empty():
            print(-1)
            return
        print(self.ddeque[self.no - 1])

test = dequeMgmt()

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        test.push_f(int(command[1]))

    elif command[0] == 'push_back':
        test.push_b(int(command[1]))

    elif command[0] == 'front':
        test.print_f()
    
    elif command[0] == 'back':
        test.print_b()
    
    elif command[0] == 'size':
        print(test.no)

    elif command[0] == 'empty':
        if test.is_Empty():
            print(1)
        else:
            print(0)

    elif command[0] == 'pop_front':
        test.pop_f()

    elif command[0] == 'pop_back':
        test.pop_b()
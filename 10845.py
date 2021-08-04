import sys

n = int(sys.stdin.readline().rstrip())

queue = []

for _ in range(n):
    string = sys.stdin.readline().rstrip().split()

    if string[0] == 'push':
        queue.append(int(string[1]))

    elif string[0] == 'pop':
        if len(queue) == 0:
            print(-1)
            continue
        
        print(queue[0])
        del queue[0]
    
    elif string[0] == 'size':
        print(len(queue))

    elif string[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif string[0] == 'front':
        if len(queue) == 0:
            print(-1)
        
        else:
            print(queue[0])

    elif string[0] == 'back':
        if len(queue) == 0:
            print(-1)
        
        else:
            print(queue[-1])
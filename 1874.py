import sys

res = [int(sys.stdin.readline().rstrip()) for _ in range(int(input()))]
stack = []
stack2 = []
stack3 = []
count = 0
t = 1


while count < len(res):

    if len(stack) == 0:
        
        stack.append(t)
        t += 1
        stack3.append('+')
        continue
    
    if stack[-1] != res[count]:
        if len(stack) > len(res):
            break
        stack.append(t)
        t += 1
        stack3.append('+')
    
    elif stack[-1] == res[count]:
        count += 1
        stack2.append(stack.pop())        
        stack3.append('-')

if stack2 == res:
    for i in stack3:
        print(i)
else:
    print("NO")
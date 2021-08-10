import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    string = sys.stdin.readline().rstrip()

    bracket = []

    for t in string:
        if t == '(':
            bracket.append(t)

        elif t == ')':
            if len(bracket) > 0 and bracket[-1] == '(':
                bracket.pop()
            else:
                bracket.append(t)

    if len(bracket) == 0:
        print("YES")
    
    else:
        print("NO")

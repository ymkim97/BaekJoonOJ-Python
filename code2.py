a = []

while True:
    n = int(input())
    
    if n != 0:
        a.append(n)

    else:

        index = int(input())
        num = int(input())
        if index < 0:
            index = len(a) + index

        if index >= len(a):
            print("Not in range")
            break

        else:
            for i in range(0, index + 1):
                if a[i] > num:
                    print(a[i])            
            break
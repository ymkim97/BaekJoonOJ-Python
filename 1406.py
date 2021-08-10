#시간 해결

import sys

Leftstack = list(sys.stdin.readline().rstrip())

command_number = int(sys.stdin.readline().rstrip())

Rightstack = []

for _ in range(command_number):
    
    string = sys.stdin.readline().rstrip().split()
    
    if string[0] == 'L' and len(Leftstack) != 0:
        Rightstack.append(Leftstack.pop())

    elif string[0] == 'D' and len(Rightstack) != 0:
        Leftstack.append(Rightstack.pop())

    elif string[0] == 'P':
        Leftstack.append(string[1])

    elif string[0] == 'B' and len(Leftstack) != 0:
        Leftstack.pop()

while len(Rightstack) != 0:
    Leftstack.append(Rightstack.pop())        

print("".join(Leftstack))   

""" 시간 Over 2ms
import sys

string = list(sys.stdin.readline().rstrip())

command_number = int(sys.stdin.readline().rstrip())

cursor = len(string)
backup = []

for _ in range(command_number):
    command = sys.stdin.readline().rstrip().split()
    
    if command[0] == 'P':
        command_2 = command[1]

        for _ in range(len(string) - cursor):
            backup.append(string.pop())

        string.append(command_2)

        while len(backup):
            string.append(backup.pop())

        cursor += 1

    elif command[0] == 'L':
        
        if cursor - 1 < 0:
            continue
        
        cursor -= 1
        
    
    elif command[0] == 'D':
        if cursor + 1 > len(string):
            continue    

        cursor += 1
    
    elif command[0] == 'B':
        if cursor == 0:
            continue
        
        for _ in range(len(string) - cursor):
            backup.append(string.pop())

        string.pop()

        while len(backup):
            string.append(backup.pop())

        cursor -= 1

print("".join(string))

"""
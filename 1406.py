import sys

string = sys.stdin.readline().rstrip()

command_number = int(sys.stdin.readline().rstrip())

backup = []

for i in range(command_number):
    command = sys.stdin.readline().rstrip().split()

    if command == 'P':
        command_2 = command[1]
        string.append(command_2)

    elif command == 'L':
        

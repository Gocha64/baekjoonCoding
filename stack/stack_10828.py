import sys


stack = []

def Push(x):
    stack.append(x)

def Pop():
    if Size() == 0:
        print(-1)
    else:
        print(stack[len(stack)-1])
        stack.pop()


def Size():
    return len(stack)

def Empty():
    if Size() == 0:
        return 1
    else:
        return 0

def Top():
    if Empty() == 0:
        return stack[len(stack)-1]
    else:
        return -1



comSize = int(input())

for _ in range(comSize):
    com= sys.stdin.readline().rstrip()

    if "push" in com:
        x = com.split()[1]
        Push(x)
    elif com == "pop":
        Pop()
    elif com == "size":
        print(Size())
    elif com == "empty":
        print(Empty())
    elif com == "top":
        print(Top())
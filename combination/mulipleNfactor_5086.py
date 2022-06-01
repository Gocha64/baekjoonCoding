

def relation(a, b):

    if a == 0 and b == 0:
        return False

    if b % a == 0:
        print("factor")
        return True
    elif a % b == 0:
        print("multiple")
        return True
    else:
        print("neither")
        return True

while True:
    a, b = map(int, input().split())
    if not relation(a, b):
        break
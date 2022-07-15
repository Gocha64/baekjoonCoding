n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

a.sort()

def binary_search(num):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == num:
            return 1

        elif a[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return 0


for i in b:
    print(binary_search(i))



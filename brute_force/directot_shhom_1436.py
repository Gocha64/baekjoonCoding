n = int(input())

count = 0
number = 666

while True:
    if str(number).find("666") != -1:
        count += 1
        if count == n:
            break
    number += 1

print(number)
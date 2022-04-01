import math

r = int(input())

euclid_circle = math.pi * r * r

euclid_circle= round(euclid_circle, 6)
taxicap_circle = r * r * 2
print(f'{euclid_circle:.6f}')
print(f'{taxicap_circle:.6f}')
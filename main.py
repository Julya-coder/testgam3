a = int(input())
max = -9999999
for i in range(a):
    f = int(input())
    if f % 10 == 2 and f > max:
        max = f
print(max)




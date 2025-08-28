N = int(input()())
D = int(input()())

count = 0
while N > 0:
    if N % 10 == D:
        count += 1
    N //= 10

print(count)

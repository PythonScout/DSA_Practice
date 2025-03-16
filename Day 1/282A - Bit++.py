#282A - Bit++
n = int(input())
x = 0
while n > 0:
    n -= 1
    statement = list(input().strip())  # Strip spaces to avoid indexing errors
    if statement[1] == '+':  # Corrected indexing
        x += 1
    else:
        x -= 1
print(x)
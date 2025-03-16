matrix = [list(map(int, input().split())) for _ in range(5)]

for m in range(5):
    for n in range(5):
        if(matrix[m][n] == 1):
            sol = abs(2-m)+abs(2-n)
            break
print(sol)
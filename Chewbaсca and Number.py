def invert(t):
    return str(ord('9') - ord(t))
 
x = list(input())
for i in range(len(x)):
    if(i == 0):
        if(x[i] == '9'): #skip to avoid making 0
            continue
    y = invert(x[i])
    if(int(x[i]) > int(y)):
        x[i] = y
print(''.join(x))
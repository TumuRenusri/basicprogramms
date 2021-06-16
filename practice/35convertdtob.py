def conve(x):
    if x>1:
        conve(x//2)
    print(x%2,end='')
conve(int(input()))